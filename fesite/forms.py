from django import forms
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-floating form-floating mb-3', 'required': True}))
    class Meta:
        model = Contact
        fields = "__all__"
        widgets ={
            'name' : forms.TextInput(attrs={'class': 'form-control form-floating form-floating focus-visible mb-3', 'required':True}),
            'email' : forms.TextInput(attrs={'class': 'form-control form-floating form-floating mb-3', 'required':True}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control form-floating form-floating mb-3', 'max_length': 13, 'required': True}),
            'message' : forms.TextInput(attrs={'class': 'form-control form-floating form-floating mb-3'}),      
        }    