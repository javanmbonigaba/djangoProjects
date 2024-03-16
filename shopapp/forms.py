from django import forms
from .models import Buyer
from django.contrib.auth.models import User
class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control mb-3'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'phone' : forms.NumberInput(attrs={'class' : 'form-control'}),

        }

        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'phone' : 'Telephone',
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
