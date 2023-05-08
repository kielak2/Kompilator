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



class SectionType(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SectionStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StatusData(models.Model):
    error_message = models.TextField(blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.error_message or str(self.line_number)

class FileSection(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    start_line = models.IntegerField()
    start_char = models.IntegerField(blank=True, null=True)
    end_line = models.IntegerField()
    end_char = models.IntegerField(blank=True, null=True)
    section_type = models.ForeignKey(SectionType, on_delete=models.CASCADE)
    section_status = models.ForeignKey(SectionStatus, on_delete=models.CASCADE)
    status_data = models.ForeignKey(StatusData, on_delete=models.CASCADE)
    content = models.TextField()
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='sections')
    is_available = models.BooleanField(default=True)
    availability_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name or self.section_type