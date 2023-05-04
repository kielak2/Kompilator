from django import forms
from .models import Directory
class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
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