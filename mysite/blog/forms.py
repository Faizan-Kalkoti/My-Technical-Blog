from django import forms
from blog.models import Post, Comments

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text', 'post_img')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
        }

class CommentsForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea commentformtext'})
        }
