from django import forms
from django.forms import ModelForm
from.models import post, about


# create post form

class postForm(ModelForm):
    class Meta:
        model = post
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'العنوان'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الكاتب'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نص  المقال'}),
        }



# create about form

class aboutForm(ModelForm):
    class Meta:
        model = about
        fields = "__all__"
        widgets = {
            'about_me': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'من أنا؟'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'التعليم'}),
            'intrests': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' الاهتمامات'}),
        }