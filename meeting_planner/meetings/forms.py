from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput
from django.core.exceptions import ValidationError

from .models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start': TimeInput(attrs={'type': 'time'}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"}),
            'comment': TextInput(attrs={"type": "text"}),
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meeting date cannot be in the past")
        return d
    