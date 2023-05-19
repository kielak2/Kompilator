from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Directory, File
from multiupload.fields import MultiFileField

class UploadFileForm(forms.Form):
    file = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
    directory = forms.ModelChoiceField(queryset=Directory.objects.all())

class AddDirectoryForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))
    parent_directory = forms.ModelChoiceField(required=False, queryset=Directory.objects.all())

    class Meta:
        model = Directory
        fields = ['name', 'description', 'parent_directory']
        labels = {
            'name': 'Directory name',
            'description': 'Description (optional)',
            'parent_directory': 'Parent directory (optional)'
        }

class DeleteDirectoryForm(forms.Form):
    directory = forms.ModelChoiceField(queryset=Directory.objects.all())

class DeleteFileForm(forms.Form):
    file = forms.ModelChoiceField(queryset=File.objects.all())


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })