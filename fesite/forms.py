from django import forms
from django.forms import widgets
from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    class Meta:
        model = Contact
        fields = "__all__"
        widgets ={
            'name' : forms.TextInput(attrs={'class': 'form-control', 'required':True}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'required':True}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control', 'max_length': 13, 'required': True}),
            'message' : forms.TextInput(attrs={'class': 'form-control'}),      
        }