from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import Office_Types
from django.forms import ModelChoiceField

at_obj = Office_Types()

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
       
        pass


class AvailabilityForm(forms.Form):
    office_type = ModelChoiceField(queryset=Office_Types.objects.all())
    start_datetime = forms.DateTimeField(required=True,
                                              widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.DateTimeField(required=True, 
                                            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))