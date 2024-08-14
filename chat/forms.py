from django import forms
from chat.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'file']  # 'text' va 'file' maydonlarini qo‘shing
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Xabarni kiriting...'}),
        }
