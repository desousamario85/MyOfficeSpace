from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import Category

at_obj = Category()

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
       
        pass


class AvailabilityForm(forms.Form):
    category_name = forms.CharField(widget=forms.ChoiceField(choices=at_obj.get_types()))
    start_datetime = forms.SplitDateTimeField(required=True,
                                              widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.SplitDateTimeField(required=True, 
                                            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))