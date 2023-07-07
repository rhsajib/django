from django import forms
from .models import Contact, Post




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    phone = forms.CharField(max_length=100, label='Your Phone')
    content = forms.CharField(max_length=100, label='Your Details')


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['id', 'slug', 'created_at']