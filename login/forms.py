from django import forms
from models import sign_up
class signup_form(forms.ModelForm):
    class Meta:
        model = sign_up
        fields = ['username','name','email','password']

