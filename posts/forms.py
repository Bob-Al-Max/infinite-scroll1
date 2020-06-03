from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        'Topic',
        'jfjfkfkfk',
        'settings.EMAIL_HOST_USER',
        ['borq_10@mail.ru'],
        fail_silently=False,

        
        