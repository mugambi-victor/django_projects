from django import forms
from .models import FormData

class FormSubmitForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name', 'email', 'message']
