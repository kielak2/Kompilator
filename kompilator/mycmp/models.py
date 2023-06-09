from django.db import models
from django.contrib.auth.models import User

class Directory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    availability_changed_date = models.DateTimeField(auto_now=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    parent_directory = models.ForeignKey('self', null=True, blank=True, related_name='subdirectories', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    last_changed_accessibility = models.DateTimeField(auto_now=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name='files')
    file_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class FileSection(models.Model):
    name = models.CharField(max_length=32, null=True)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateField(auto_now=True)
    begin = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)