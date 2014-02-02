from django import forms
from django.conf import settings
from django.db.models import Q
from django.core.context_processors import request
from django.core.files.images import get_image_dimensions
from django.forms import extras
from dirplace.models import UserProfile, Occupation
from datetime import date
from captcha.fields import CaptchaField
from userena import views as userena_forms

class ContactForm(forms.Form):
    name =  forms.CharField(max_length=81)
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

class EditProfileForm(userena_forms.EditProfileForm):
    birth_date = forms.DateTimeField (required=False, widget=extras.SelectDateWidget(years=range(date.today().year - 11,date.today().year - 106,-1)))
    privacy = forms.CharField(widget=forms.HiddenInput(), initial='registered')