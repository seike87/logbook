from django import forms
from django.forms import ModelForm
from .models import Logs

class LogForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Logs
        fields = '__all__'
        widgets = {
            #'zeitstempel' :forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'})
            'datum': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'name': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Name'}),
            'vorname': forms.TextInput(attrs={'class': 'input', 'type': 'text'}),
            'ziel': forms.TextInput(attrs={'class': 'input', 'type': 'text'}),
            'grund': forms.TextInput(attrs={'class': 'input', 'type': 'text'}),
            'von': forms.TimeInput(attrs={'class': 'input', 'type': 'time'}),
            'bis': forms.TimeInput(attrs={'class': 'input', 'type': 'time'}),
            'kostenstelle': forms.TextInput(attrs={'class': 'input', 'type': 'text'}),
            'projekt': forms.TextInput(attrs={'class': 'input', 'type': 'text'}),
                  }

#    def __init__(self, *args, **kwargs):
#            super(LogForm, self).__init__(*args, **kwargs)
#            self.fields['datum'].widget.attrs.update({'class': 'input'})
#            self.fields['name'].widget.attrs.update({'class': 'input'})
#            self.fields['vorname'].widget.attrs.update({'class': 'input'})
#            self.fields['ziel'].widget.attrs.update({'class': 'input'})
#            self.fields['grund'].widget.attrs.update({'class': 'input'})
#            self.fields['von'].widget.attrs.update({'class': 'input'})
#            self.fields['bis'].widget.attrs.update({'class': 'input'})
#            self.fields['kostenstelle'].widget.attrs.update({'class': 'input'})
#            self.fields['projekt'].widget.attrs.update({'class': 'input'})
