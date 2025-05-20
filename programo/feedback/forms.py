from django import forms
from .models import Feedback



class FeedbackForm(forms.ModelForm):
    session_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type' : 'datetime-local'})
    )

    class Meta:
        model = Feedback
        fields = ['pacient', 'session_date', 'message']