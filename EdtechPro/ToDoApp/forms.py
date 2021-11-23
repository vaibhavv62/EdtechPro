from django import forms
from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date_time':forms.DateInput(attrs={'type':'datetime-local'}),
            'details':forms.Textarea()
        }