from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['title', 'match_date', 'match_time', 'location', 'description']

        widgets = {
            'match_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={"type": "date"}),
            'match_time': forms.TimeInput(
                attrs={"step": "300", "type": "time"}
            ),
            'description': forms.Textarea(),
        }

        labels = {
            'match_date': "Date",
            'match_time': "Time"
        }