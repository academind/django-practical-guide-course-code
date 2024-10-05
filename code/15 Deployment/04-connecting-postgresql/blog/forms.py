from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
          "user_name": "Your Name",
          "user_email": "Your Email",
          "text": "Your Comment"
        }