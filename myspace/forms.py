from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class AvailabilityForm(forms.Form):
    start_datetime = forms.SplitDateTimeField(required=True,
                                              widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.SplitDateTimeField(required=True, 
                                            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))