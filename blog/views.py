import uuid
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm, NewPostForm
from django.db.models import Q
from django.utils.text import slugify
from django.template import RequestContext


class PostList(generic.ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 6

    def get(self, request):
        query = request.GET.get('query', '')
        category_id = request.GET.get('category', 0)
        categories = Category.objects.all()
        category_colors = {category.id: get_category_color(category.id)
                           for category in categories}
        post_list = Post.objects.all()

        if category_id:
            post_list = post_list.filter(category_id=category_id)

        if query:
            post_list = post_list.filter(Q(name__icontains=query) |
                                         Q(description__icontains=query))

        return render(request, 'index.html', {
            'post_list': post_list,
            'query': query,
            'categories': categories,
            'category_id': int(category_id),
            'category_colors': category_colors,
        })


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class NewPost(View):
    def get(self, request):
        form = NewPostForm()
        return render(request, 'new_post.html', {'form': form})

    def post(self, request):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            unique_id = uuid.uuid4().hex[:5]
            post.slug = f"{slugify(post.title)}-{unique_id}"
            post.save()

            return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))

        return render(request, 'new_post.html', {'form': form})


class EditPost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if request.user == post.author:
            form = NewPostForm(instance=post)
            return render(request, 'new_post.html', {'form': form, 'post': post, 'editing': True})
        else:
            return redirect('post_detail', slug=slug)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if request.user == post.author:
            form = NewPostForm(request.POST, instance=post)
            if form.is_valid():
                edited_post = form.save(commit=False)
                unique_id = uuid.uuid4().hex[:5]
                edited_post.slug = f"{slugify(edited_post.title)}-{unique_id}"
                edited_post.save()
                return redirect('post_detail', slug=edited_post.slug)
            else:
                return render(request, 'new_post.html', {'form': form, 'post': post, 'editing': True})
        else:
            return redirect('post_detail', slug=slug)


class DeletePost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'post_delete.html', {'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        if request.user == post.author:
            post.delete()
            return redirect('home')
        else:
            return redirect('post_detail', slug=slug)


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(
        category=category).order_by('-created_on')
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'category': category,
        'posts': posts,
        'categories': categories,
    })


def get_category_color(category_id):
    category_colors = {
        1: "#FF5733",
        2: "#FFAF33",
        3: "#A5FF33",
        4: "#33FF93",
        5: "#33F3FF",
        6: "#3355FF",
        7: "#9F33FF",
        8: "#FC33FF",
        9: "#FF3396",
    }

    return category_colors.get(category_id, "#FFFFFF")


def handler404(request, exception):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response
