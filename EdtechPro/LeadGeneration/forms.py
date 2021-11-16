from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        labels = {
            'mobile_number2':'Alternative Number',
            'stream':'Stream/Branch'
        }
        widgets = {
            'current_status_notes':forms.Textarea(),
        }