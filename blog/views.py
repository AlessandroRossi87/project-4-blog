from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category, active=True)

    return render(request, 'index.html', {
        'category': category,
        'posts': posts,
    })
