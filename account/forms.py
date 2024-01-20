from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from membership.models import MemberProfile

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'gender']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class MemberSignupForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['gender', 'phone_number', 'address', 'city','state', 'zip_code', 'country', 'date_of_birth', 'profile_pic']