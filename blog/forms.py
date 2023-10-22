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
        fields = ['title', 'slug', 'featured_image',
                  'excerpt', 'content', 'category', 'status']

# class NewPostForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ('category', 'title', 'content', 'featured_image',)
#        widgets = {
#            'category': forms.Select(attrs={
#                'class': INPUT_CLASSES
#            }),
#            'title': forms.TextInput(attrs={
#                'class': INPUT_CLASSES
#            }),
#            'content': forms.Textarea(attrs={
#                'class': INPUT_CLASSES
#            }),
#            'featured_image': forms.FileInput(attrs={
#                'class': INPUT_CLASSES
#            })
#        }


# class EditPostForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ('title', 'content', 'featured_image',)
#        widgets = {
#            'title': forms.TextInput(attrs={
#                'class': INPUT_CLASSES
#            }),
#            'content': forms.Textarea(attrs={
#                'class': INPUT_CLASSES
#            }),
#            'featured_image': forms.FileInput(attrs={
#                'class': INPUT_CLASSES
#            })
#        }
