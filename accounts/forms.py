from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.Form):
    
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Username', 'style':'width:300px'}
        )
    )
    
    email = forms.EmailField(
        required=False,
        label='Email:',
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'Email', 'style':'width:300px'}
        )
    )
    
    first_name = forms.CharField(
        required=False,
        label='First Name:',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'First Name', 'style':'width:300px'}
        )
    )
    
    last_name = forms.CharField(
        required=False,
        label='Last Name:',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Last Name', 'style':'width:300px'}
        )
    )
    
    password = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Password', 'style':'width:300px'}
        )
    )
    
    password2 = forms.CharField(
        label='Confirmation password:',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Confirmation password', 'style':'width:300px'}
        )
    )
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('Username already exists')
        return username
    
    def clean(self):
        data = super().clean()
        p1 = data.get('password')
        p2 = data.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError("Passwords don't match. ")

    
        
class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Username', 'style':'width:300px'}
        )
    )
    
    password = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Password', 'style':'width:300px'}
        )
    )
    
    