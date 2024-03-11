from django import forms
from .models import Conference

class ConferenceRegistrationForm(forms.Form):
    conference = forms.ModelChoiceField(queryset=Conference.objects.all(), label="Select Conference")