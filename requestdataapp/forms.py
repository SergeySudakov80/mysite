from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

class UserBioForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label='Your age', min_value=1, max_value=100)
    bio = forms.CharField(label='Biography', widget=forms.Textarea)

def validata_file_name(file: InMemoryUploadedFile) -> None:
    if file.name and file.size > 1048576:
        raise ValidationError('The file size is more then 1Mb. Upload was not successfully.')

class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validata_file_name])
