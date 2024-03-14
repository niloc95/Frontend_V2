from django import forms
from django.forms import widgets
from .models import Contact
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']
        widgets ={
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'phone_number': forms.TextInput(attrs={'required': True}),
            'message': forms.Textarea(attrs={'required': True}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            return phone_number  # Allow empty phone number
        phone_regex = r'^(\+?27\s?|0)(\d{2}\s?\d{3}\s?\d{4})$'
        if not re.match(phone_regex, phone_number):
            raise ValidationError("Phone number must be entered in the format: '+27 76 829 7070'")
        return phone_number