from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+\d{2} \d{2} \d{3} \d{4}$',
        message="Phone number must be entered in the format: '+27 76 829 7070'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True, help_text="Optional")
    message = models.TextField()
    #timestamp = models.DateTimeField(auto_now_add=True)
    
   

    def __str__(self):
        return self.name
