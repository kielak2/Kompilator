# Generated by Django 4.2 on 2023-05-08 20:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mycmp", "0005_file_file_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="file",
        ),
    ]
