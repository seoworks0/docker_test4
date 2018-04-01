from django import forms
from .models import Text_input


class Plus1_Form(forms.ModelForm):

    class Meta:
        model = Text_input
        fields='__all__'#('title','text','date')
