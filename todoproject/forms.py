
from django import forms

from todoapp.models import Lists


class TodoForm(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['name', 'order', 'date']


