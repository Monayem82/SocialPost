from django import forms
from . models import TwieetModel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class TwieetForm(forms.ModelForm):
    class Meta:
        model=TwieetModel
        fields=['text','photos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RegisterUser(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class loginUserForm(AuthenticationForm):
    class Meta:
        model=User
        fields=('username','password')

    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        for field_name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class profileForm(forms.ModelForm):
    pass