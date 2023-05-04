from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from mycmp.models import Directory, File


class Command(BaseCommand):
    def handle(self, *args, **options):
        File.objects.all().delete()
        Directory.objects.all().delete()
        User.objects.all().delete()
        # Create example user
        user = User.objects.create_user(username='testuser', password='testpass')

        # Create example directories
        dir1 = Directory.objects.create(name='Directory 1', description='Description 1', owner=user)
        dir2 = Directory.objects.create(name='Directory 2', description='Description 2', owner=user)
        dir3 = Directory.objects.create(name='Directory 3', owner=user, parent_directory=dir1)
        dir4 = Directory.objects.create(name='Directory 4', owner=user, parent_directory=dir3)
        dir5 = Directory.objects.create(name='Directory 5', owner=user, parent_directory=dir4)
        dir6 = Directory.objects.create(name='Directory 6', owner=user, parent_directory=dir5)

        file1 = File.objects.create(name='File1', description='This is file 1', owner=user, directory=dir1)
        file2 = File.objects.create(name='File2', description='This is file 1', owner=user, directory=dir3)
        file3 = File.objects.create(name='File3', description='This is file 1', owner=user, directory=dir3)

        # Print success message
        self.stdout.write(self.style.SUCCESS('Successfully created example data'))