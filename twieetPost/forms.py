from django import forms
from . models import TwieetModel

class TwieetForm(forms.ModelForm):
    class Meta:
        model=TwieetModel
        fields=['text','photos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'