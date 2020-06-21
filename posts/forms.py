import django.forms as forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_name','post_text','post_pubdate']
        widgets = {
            'post_name': forms.TextInput(attrs={
                'class':'formFielf',
                'name':'post_name',
                'id':'post_name',
                'placeholder':'Type title for new post'
            }),
            'post_text': forms.TextInput(attrs={
                'class': 'formFielf',
                'name': 'post_text',
                'id': 'post_text',
                'placeholder': 'New post txt'
            }),
            'post_pubdate': forms.DateTimeInput(attrs={
                'class': 'formFielf',
                'name': 'post_pubdate',
                'id': 'post_pubdate',
                'placeholder': 'datetime'
            })
        }