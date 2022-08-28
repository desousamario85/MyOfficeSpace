from django import forms


class AvailabilityForm(forms.Form):
    start_datetime = forms.SplitDateTimeField(required=True)
    end_datetime = forms.SplitDateTimeField(required=True)