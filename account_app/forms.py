from django.forms import Form, CharField, EmailField, TextInput, PasswordInput, EmailInput


class SignUpForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-75',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-75',
    }))
    email = EmailField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control w-75',
    }))
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control w-75',
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control w-75',
    }))

class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-50',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-50',
    }))