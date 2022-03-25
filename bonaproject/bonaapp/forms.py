from django import forms
from .models import Order


class CrateOrder(forms.ModelForm):
    address = forms.CharField(help_text='address', widget=forms.TextInput(attrs={'class':'input', 'name':'address'}))
    email = forms.EmailField(help_text='email', widget=forms.EmailInput(attrs={'class':'input', 'name':'email'}))
    telephone_number = forms.IntegerField(help_text='number', widget=forms.TextInput(attrs={'class':'input', 'name':'telephone_number'}))

    class Meta:
        model = Order
        fields = ['address','email','telephone_number']