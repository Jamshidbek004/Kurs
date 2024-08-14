from django import forms
from oquvchi.models import Oquvchi


class OquvchiForm(forms.ModelForm):
    class Meta:
        model = Oquvchi
        fields = ['telraqam', 'bio', 'yonalish']



