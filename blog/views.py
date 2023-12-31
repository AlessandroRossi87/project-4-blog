import uuid
import cloudinary.uploader
from cloudinary.uploader import upload
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm, NewPostForm
from django.db.models import Q
from django.utils.text import slugify
from django.template import RequestContext

# Displays all Alerts


class PostList(generic.ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 6

    def get(self, request):
        query = request.GET.get('query', '')
        category_id = request.GET.get('category', 0)
        categories = Category.objects.all()
        post_list = Post.objects.all()

        # Filters Alerts by category
        if category_id:
            post_list = post_list.filter(category_id=category_id)

        if query:
            post_list = post_list.filter(Q(name__icontains=query) |
                                         Q(description__icontains=query))

        # Renders the Index template with filtered posts
        return render(request, 'index.html', {
            'post_list': post_list,
            'query': query,
            'categories': categories,
            'category_id': int(category_id),
        })

# Displays Alert Detail


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Gets one Alert and the comments for it
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False

        # Checks if user has liked the Alert
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Renders the Alert Detail page
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
        # Retrieve an Alert and the relative comments
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        # Checks if user has liked this Alert
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        # Saves the comment or goes back to Alert Detail
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        # Renders the Alert Detail page after commenting
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

# Creates a new Alert


class NewPost(View):
    def get(self, request):
        form = NewPostForm()
        return render(request, 'new_post.html', {'form': form})

    def post(self, request):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Saves the Alert and gives it a unique slug
            post = form.save(commit=False)
            post.author = request.user
            unique_id = uuid.uuid4().hex[:5]
            post.slug = "{}-{}".format(slugify(post.title), unique_id)
            post.save()

            # Redirects the user to the Alert Detail page
            return HttpResponseRedirect(reverse(
                'post_detail', args=[post.slug]))

        # Renders the new Alert page if form is not valid
        return render(request, 'new_post.html', {'form': form})

# Edits an Alert


class EditPost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        # Authorizes author to edit the Alert
        if request.user == post.author:
            form = NewPostForm(instance=post)
            return render(request, 'new_post.html', {
                'form': form, 'post': post, 'editing': True})
        else:
            return redirect('post_detail', slug=slug)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if request.user == post.author:
            form = NewPostForm(request.POST, instance=post)
            if form.is_valid():
                edited_post = form.save(commit=False)
                unique_id = uuid.uuid4().hex[:5]
                edited_post.slug = "{}-{}".format(
                    slugify(post.title), unique_id)

                # Enables editing of image
                if 'featured_image' in request.FILES:
                    edited_image = request.FILES['featured_image']
                    uploaded_image = upload(edited_image)
                    edited_post.featured_image = uploaded_image['url']

                # Saves Alert and redirects to Alert Detail Page
                edited_post.save()
                return redirect('post_detail', slug=edited_post.slug)
            else:
                return render(request, 'new_post.html', {
                    'form': form, 'post': post, 'editing': True})
        else:
            return redirect('post_detail', slug=slug)


# Deletes an Alert
class DeletePost(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'post_delete.html', {'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        # Authorizes author to delete the Alert
        if request.user == post.author:
            # Deletes the Alert and redirects to Home Page
            post.delete()
            return redirect('home')
        else:
            return redirect('post_detail', slug=slug)


# Likes an Alert
class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Filters Alert according to category
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(
        category=category).order_by('-created_on')
    categories = Category.objects.all()

    # Renders the Home page with only filtered Alerts
    return render(request, 'index.html', {
        'category': category,
        'posts': posts,
        'categories': categories,
    })


# Renders custom 404 template
def handler404(request, exception):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response
