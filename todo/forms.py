from django import forms

class RegisterForm(forms.Form):
        username = forms.EmailField(label='Username / Email')
        password = forms.CharField(label='Password', widget=forms.PasswordInput)
        first_name = forms.CharField(label='First name') 
        last_name = forms.CharField(label='Last name')


class LoginForm(forms.Form):
        username = forms.EmailField(label='Username / Email')
        password = forms.CharField(label='Password', widget=forms.PasswordInput)
