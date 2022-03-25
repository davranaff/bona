from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(help_text='you\'r username',error_messages={'invalid':'поле неправильно заполнено'} , widget=forms.TextInput(attrs={'class':'input my-3','placeholder':'write here...'}))
    email = forms.EmailField(help_text='you\'r mail',error_messages={'invalid':'поле неправильно заполнено'}, widget=forms.EmailInput(attrs={'class':'input my-3','placeholder':'write here...'}))
    password1 = forms.CharField(help_text='you\'r password',error_messages={'invalid':'поле неправильно заполнено'}, widget=forms.PasswordInput(attrs={'class':'input my-3','placeholder':'write here...'}))
    password2 = forms.CharField(help_text='confirm password',error_messages={'invalid':'поле неправильно заполнено'}, widget=forms.PasswordInput(attrs={'class':'input my-3','placeholder':'write here...'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']