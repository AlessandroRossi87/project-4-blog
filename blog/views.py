from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm, NewPostForm
from django.db.models import Q


class PostList(generic.ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

    # def get_queryset(self):
    #    queryset = Post.objects.filter(status=1).order_by('-created_on')
    #    category_id = self.request.GET.get('category')
    #    if category_id:
    #        queryset = queryset.filter(category_id=category_id)
    #
    #    return queryset

    def posts(self, request):
        query = request.GET.get('query', '')
        category_id = request.GET.get('category', 0)
        categories = Category.objects.all()
        posts = Post.objects.filter(is_sold=False)

        if category_id:
            posts = posts.filter(category_id=category_id)

        if query:
            posts = posts.filter(Q(name__icontains=query) |
                                 Q(description__icontains=query))

        return render(request, 'index.html', {
            'posts': posts,
            'query': query,
            'categories': categories,
            'category_id': int(category_id)
        })


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
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
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
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
                form.save()
                return redirect('post_detail', slug=slug)
        else:
            return redirect('post_detail', slug=slug)


class DeletePost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

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
        category=category, status=1).order_by('-created_on')
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'category': category,
        'posts': posts,
        'categories': categories,
    })


# @login_required
# def new(request):
#    if request.method == 'POST':
#        form = NewPostForm(request.POST, request.FILES)
#
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.created_by = request.user
#            post.save()
#
#            return redirect('post_detail', pk=post.id)
#    else:
#        form = NewPostForm()
#
#    return render(request, 'form.html', {
#        'form': form,
#        'title': 'Post new Alert',
#    })
