from .models import Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content', 'category'] #slug
