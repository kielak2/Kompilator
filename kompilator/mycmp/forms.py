from django import forms
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