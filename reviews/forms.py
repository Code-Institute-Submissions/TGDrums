from django import forms
from .models import Post


class ReviewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')