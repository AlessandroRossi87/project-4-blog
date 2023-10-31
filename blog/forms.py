from .models import Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'content', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
