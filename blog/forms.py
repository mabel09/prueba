from django import forms
from django.forms import ModelForm
from models import Post

class PostForm(ModelForm):
    title = forms.CharField(max_length=50, label='Titulo')
    date = forms.DateTimeField(required=True,
                               help_text='mm/dd/aaaa 24:00',
                               label='Fecha y hora')
    body = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post

