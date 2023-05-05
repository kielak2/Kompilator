from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Directory
from .models import File
from .forms import UploadFileForm, AddDirectoryForm, DeleteDirectoryForm, DeleteFileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def awww1(request):
    files = File.objects.all()
    directories = Directory.objects.all()
    directories = directories.filter(parent_directory__isnull=True)
    return render(request, 'mycmp/awww1.html', {'directories': directories, 'files': files})

def upload_file(request):
    directories=Directory.objects.all()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            dir1 = form.cleaned_data['directory']
            username = 'testuser'
            user = User.objects.get(username=username)
            files = request.FILES.getlist('file')

            for file in files:
                file_obj = File.objects.create(name=str(file), description='This is file', owner=user, directory=dir1, file=file)
                file_obj.save()

            return redirect('aww1')
    else:
        form = UploadFileForm()
    return render(request, 'mycmp/upload.html', {'form': form, 'directories': directories})

def delete_file(request):
    files = File.objects.all()
    if request.method == 'POST':
        form = DeleteFileForm(request.POST)
        if form.is_valid():
            file = form.cleaned_data['file']
            file.delete()
            return redirect('aww1')
    else:
        form = DeleteFileForm()
    return render(request, 'mycmp/delete_file.html', {'form': form, 'files': files})


def add_directory(request):
    directories = Directory.objects.all()
    if request.method == 'POST':
        form = AddDirectoryForm(request.POST)
        if form.is_valid():
            directory = form.save(commit=False)
            username = 'testuser'
            user = User.objects.get(username=username)
            directory.owner = user # set the owner to the logged-in user
            directory.save()
            return redirect('aww1')
    else:
        form = AddDirectoryForm()
    return render(request, 'mycmp/add_directory.html', {'directories': directories})

def delete_directory(request):
    directories = Directory.objects.all()
    if request.method == 'POST':
        form = DeleteDirectoryForm(request.POST)
        if form.is_valid():
            dir = form.cleaned_data['directory']
            dir.delete()
            return redirect('aww1')
    else:
        form = DeleteDirectoryForm()
    return render(request, 'mycmp/delete_directory.html', {'form': form, 'directories': directories})

def show_file_content(request):
    file = File.objects.get(pk=2)
    with open(file.file.path, 'r') as f:
        content = f.read()
    return render(request, 'mycmp/show_file_content.html', {'file': file, 'content': content})

















