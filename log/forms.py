from django import forms
from django.forms import ModelForm
from .models import Logs

class LogForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Logsfields = '__all__'