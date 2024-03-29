from django import forms
from .models import Conference, MemberProfile

class ConferenceRegistrationForm(forms.Form):
    conference = forms.ModelChoiceField(queryset=Conference.objects.all(), label="Select Conference")


class MemberProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = "__all__"
        exclude = ()
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
