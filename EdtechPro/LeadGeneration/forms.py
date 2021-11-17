from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    # required_css_class = "required"
    class Meta:

        model = Lead
        fields = '__all__'
        labels = {
            'mobile_number':'Primary Mobile Number',
            'mobile_number2':'Secondary(Alternative) Number',
            'stream':'Stream/Branch',
            'school_college':'School/College Name'
        }
        help_texts = {
            'mobile_number':'Preferred WhatsApp Number, 10 digits only!',
            'mobile_number2':'10 digits only!'
        }
        widgets = {
            'current_status_notes':forms.Textarea(),
            'email':forms.TextInput(
                attrs={
                    'placeholder':'user@domain.com'
                }
            ),
            'referred_by':forms.TextInput(attrs={'placeholder':'FullName - Batch - MobileNumber'}),
            'handled_by':forms.TextInput(attrs={'readonly':True})

        }