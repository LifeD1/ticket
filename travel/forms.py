from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import User, Agency, Bus, Trip
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    # gender = forms.ChoiceField(choices=)


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",  "email", "password1", "password2"]


class AddAgencyAdminForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    agency_id = forms.ModelChoiceField(queryset=Agency.objects.all(), to_field_name='id')
    # gender = forms.ChoiceField(choices=)


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",  "email", 'agency_id', "password1", "password2"]



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



class AddAgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'


class AddBusForm(ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'


class AddTripsForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'