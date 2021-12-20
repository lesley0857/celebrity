from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from pagedown.widgets import PagedownWidget

from.models import *
from .views import *

class create_customer(forms.ModelForm):
    #created = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Customer
        fields ='__all__'
        exclude = ['user','created']
    def phone_valid(self, request, *args, **kwargs):
        phone = self.cleaned_data.get("phone")
        if "9" in phone:
            print(phone)
        else:
            pass

class create_post(forms.ModelForm):
    #details = forms.CharField(widget=forms.TextInput)
    #filefield  = forms.CharField(widget=forms.FileInput(attrs=['multiple']))
    class Meta:
        model = Comments
        fields ='__all__'
       # exclude = ['created']