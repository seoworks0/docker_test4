from django import forms
from .models import Kyokigo_input


class Kyokigo_Form(forms.ModelForm):

    class Meta:
        model = Kyokigo_input
        fields='__all__'#('title','text','date')
