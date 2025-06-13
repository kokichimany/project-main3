from django import forms
from .models import Comment, Post, PostComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class PostCommentForm(forms.ModelForm):  
    class Meta:
        model = PostComment
        fields = ['text']
