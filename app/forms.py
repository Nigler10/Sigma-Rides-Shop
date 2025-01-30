from django import forms
from .models import Comment, Review

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']  # Only allow users to input the comment body

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['feedback']

