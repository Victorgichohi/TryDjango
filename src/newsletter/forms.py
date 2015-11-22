from django import forms

from .models import SignUP

class ContactForm(forms.Form):
    full_name=forms.CharField()
    email=forms.EmailField()
    message = forms.CharField()

class SignUPForm(forms.ModelForm):
    class Meta:
        model=SignUP
        fields = ["full_name","email"]
    def clean_email(self):
        email =self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain,extension = provider.split('.')
        if not domain == 'gmail':
            raise forms.ValidationError("please make sure to use a gmail account")
        # if not extension == '.com':
        #     raise forms.ValidationError("please enter the correct email adress")
        return email
    def clean_full_name(self):
        # some validation will be here
        full_name = self.cleaned_data.get('full_name')
        return full_name
