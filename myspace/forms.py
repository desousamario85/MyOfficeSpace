from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
  
  
class ContactForm(forms.Form):
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class AvailabilityForm(forms.Form):
    start_datetime = forms.SplitDateTimeField(required=True,
                                              widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.SplitDateTimeField(required=True, 
                                            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))