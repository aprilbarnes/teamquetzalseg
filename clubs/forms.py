from django import forms
from .models import  User

class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password" , widget=forms.PasswordInput())

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','bio','personalstatement','experiencelevel']
        widgets = {'bio':forms.Textarea()}

    new_password = forms.CharField(label = 'Password',widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label = 'Password Confirmation',widget=forms.PasswordInput() )
