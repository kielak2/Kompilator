import sys
from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Directory
from .models import File
from .forms import UploadFileForm, AddDirectoryForm, DeleteDirectoryForm, DeleteFileForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import subprocess
import os

def awww1(request):
    files = File.objects.all()
    directories = Directory.objects.all()
    directories = directories.filter(parent_directory__isnull=True)
    return render(request, 'mycmp/awww1.html', {'directories': directories, 'files': files})

def runcode(request):
    files = File.objects.all()
    directories = Directory.objects.all()
    directories = directories.filter(parent_directory__isnull=True)
    if request.method == "GET":
        code = request.GET['codearea']
        standard = request.GET['standard']
        procesor = request.GET['procesor']
        optimization = request.GET['optimization']
        MCSoption = request.GET['MCSoption']
        Z80Soption = request.GET['Z80Soption']
        STMoption = request.GET["STMoption"]
        cpuoption = ""
        if (procesor == "mmcs51"):
            cpuoption = "--" + MCSoption
        elif (procesor == "mz80"):
            cpuoption = "--asm=" + Z80Soption
        elif (procesor == "mstm8")    :
            cpuoption = "--" + STMoption

        print(optimization)
        print(standard)
        print(procesor)
        print(cpuoption)
        try:
            with open('file.c', 'w') as f:
                f.write(code)

            result = subprocess.run(['sdcc', "-" + optimization, '-S', '-std=' + standard, "-" + procesor, cpuoption ,'file.c'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                output = open('file.asm', 'r').read()
            else:
                output = result.stderr.decode('utf-8')
        except Exception as e:
            output = str(e)

        os.remove('file.c')
    return render(request, 'mycmp/awww1.html',
                  {"code": code, "output": output, 'directories': directories, 'files': files})

def upload_file(request):
    directories=Directory.objects.all()
    files = File.objects.all()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            dir1 = form.cleaned_data['directory']
            username = 'testuser'
            user = User.objects.get(username=username)
            files = request.FILES.getlist('file')
            for file in files:
                content = file.read().decode("utf-8")
                file_obj = File.objects.create(name=str(file), description='This is file', owner=user, directory=dir1,
                                               file=file, file_content=content)
                file_obj.save()

            return redirect('aww1')
    else:
        form = UploadFileForm()
    return render(request, 'mycmp/upload.html', {'form': form, 'directories': directories, 'files': files})

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
    return render(request, 'mycmp/upload.html', {'form': form, 'files': files})


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
    return render(request, 'mycmp/directories_action.html', {'form': form, 'directories': directories})


















