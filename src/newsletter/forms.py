from django import forms

from .models import SignUP

class SignUPForm(forms.ModelForm):
    class meta:
        model=SignUP
        fields = ["full_name","email"]
