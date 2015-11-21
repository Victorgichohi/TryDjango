from django import forms

from .models import SignUP

class SignUPForm(forms.ModelForm):
    class meta:
        model=SignUP
        fields = ["full_name","email"]
    def clean_email(self):
        email =self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain,extension = provider.split('.')
        if not domain == 'gmail':
            raise forms.ValidationError("please make sure to use a gmail account")
        if not extension == '.com':
            raise forms.ValidationError("please enter the correct email adress")
        return email
