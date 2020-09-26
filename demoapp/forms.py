
from django import forms
from django.forms import ClearableFileInput
from .models import UploadPdf

class ResumeUpload(forms.ModelForm):

    # firstname = forms.CharField(label="Enter first name", max_length=50)
    # email = forms.EmailField(label="Enter email")

    class Meta:
        model = UploadPdf
        fields = ['resumes']
        widgets = {
            'resumes': ClearableFileInput(attrs={'multiple': True}),
        }