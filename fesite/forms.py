from django import forms
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
    class Meta:
        model = Contact
        fields = "__all__"
        widgets ={
            'name' : forms.TextInput(attrs={'required':True}),
            'email' : forms.TextInput(attrs={'required':True}),
            'phone_number' : forms.TextInput(attrs={'required': True}),
            'message' : forms.TextInput(attrs={'required': True}),      
        }    