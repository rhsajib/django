from django import forms
from .models import Contact, Post




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Name'}))
    phone = forms.CharField(max_length=100, label='Your Phone')
    content = forms.CharField(max_length=100, label='Your Details')


class ContactModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label =  'My Name'
        self.fields['phone'].initial =  '+880'
        self.fields['content'].initial =  'My content is'

    class Meta:
        model = Contact
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'}),
        #     'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Phone'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Say Something', 'rows': 5}),
        }

        # labels = {
        #     'name': 'Your Name',
        #     'phone': 'Phone Number',
        #     'content': 'Write Content',
        # }

        # help_texts = {
        #     'name': 'Your Full Name',
        #     'phone': 'Personal Phone Number',
        #     'content': 'Let Us Know Something',
        # }

    def clean_name(self):
        value = self.cleaned_data['name']
        # value = self.cleaned_data.get('name')

        num_of_words = value.split(' ')
        if len(num_of_words) > 3:
            self.add_error('name', 'Name can have maximum 3 words')
       
        return value
           



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','id', 'slug', 'created_at']
        widgets = {
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple': True
            }),
            
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple': True
            }),
        }