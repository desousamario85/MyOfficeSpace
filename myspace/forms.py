from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import Office_Spaces
from django.forms import ModelChoiceField


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    message = forms.EmailField(widget=forms.Textarea(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))

    def send_email(self):
       
        pass


class AvailabilityForm(forms.Form):
    office_name = ModelChoiceField(queryset=Office_Spaces.objects.all())
    start_datetime = forms.DateTimeField(required=True,
                                              widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_datetime = forms.DateTimeField(required=True, 
                                            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
                    