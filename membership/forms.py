from django import forms
from .models import Conference, MemberProfile

class ConferenceRegistrationForm(forms.Form):
    conference = forms.ModelChoiceField(queryset=Conference.objects.all(), label="Select Conference")


class MemberProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = "__all__"
