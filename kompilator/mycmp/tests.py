from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Directory, File
from django.urls import reverse
from .forms import UploadFileForm, AddDirectoryForm, DeleteDirectoryForm, DeleteFileForm, NewUserForm
class DirectoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        test_user = User.objects.create(username='testuser', password='12345')
        Directory.objects.create(name='Test Directory', owner=test_user)

    def test_directory_name(self):
        directory = Directory.objects.get(id=1)
        field_label = directory._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_string_representation(self):
        directory = Directory.objects.get(id=1)
        self.assertEqual(str(directory), directory.name)


class FileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        test_user = User.objects.create(username='testuser', password='12345')
        test_directory = Directory.objects.create(name='Test Directory', owner=test_user)
        File.objects.create(name='Test File', directory=test_directory, owner=test_user)

    def test_file_name(self):
        file = File.objects.get(id=1)
        field_label = file._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_string_representation(self):
        file = File.objects.get(id=1)
        self.assertEqual(str(file), file.name)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_directory = Directory.objects.create(name='testdirectory', owner=self.test_user)
        self.test_file = File.objects.create(name='testfile', owner=self.test_user, directory=self.test_directory)

        self.awww1_url = reverse('aww1')
        self.upload_file_url = reverse('upload_file')
        self.add_directory_url = reverse('add_directory')
        self.delete_directory_url = reverse('delete_directory')
        self.delete_file_url = reverse('delete_file')
        self.runcode_url = reverse('runcode')

    def test_awww1_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.awww1_url)
        self.assertEqual(response.status_code, 200)

    def test_awww1_view_unauthenticated(self):
        response = self.client.get(self.awww1_url)
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_add_directory_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.add_directory_url, {'name': 'new_directory'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Directory.objects.filter(name='new_directory').exists())

    def test_add_directory_unauthenticated(self):
        response = self.client.post(self.add_directory_url, {'name': 'new_directory'})
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertFalse(Directory.objects.filter(name='new_directory').exists())

    def test_delete_directory_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.delete_directory_url, {'directory': self.test_directory.id})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Directory.objects.filter(name='testdirectory').exists())

    def test_delete_directory_unauthenticated(self):
        response = self.client.post(self.delete_directory_url, {'directory': self.test_directory.id})
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertTrue(Directory.objects.filter(name='testdirectory').exists())

    def test_delete_file_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.delete_file_url, {'file': self.test_file.id})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(File.objects.filter(name='testfile').exists())

    def test_delete_file_unauthenticated(self):
        response = self.client.post(self.delete_file_url, {'file': self.test_file.id})
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        self.assertTrue(File.objects.filter(name='testfile').exists())

class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.directory = Directory.objects.create(name='test_dir', owner=self.user)
        self.file = File.objects.create(name='test_file', directory=self.directory, owner=self.user)

    def test_upload_file_form_valid_data(self):
        uploaded_file = SimpleUploadedFile('test_file.txt', b'This is the file content.')
        form = UploadFileForm(data={'directory': self.directory.id}, files={'file': [uploaded_file]})
        self.assertTrue(form.is_valid())
    def test_add_directory_form_valid_data(self):
        form = AddDirectoryForm(data={
            'name': 'test_directory',
            'description': 'this is a test',
            'parent_directory': self.directory.id
        })

        self.assertTrue(form.is_valid())

    def test_delete_directory_form_valid_data(self):
        form = DeleteDirectoryForm(data={
            'directory': self.directory.id
        })

        self.assertTrue(form.is_valid())

    def test_delete_file_form_valid_data(self):
        form = DeleteFileForm(data={
            'file': self.file.id
        })

        self.assertTrue(form.is_valid())

    def test_new_user_form_valid_data(self):
        form = NewUserForm(data={
            'username': 'testuser11',
            'email': 'testuser2@test.com',
            'password1': 'ABcdh123',
            'password2': 'ABcdh123'
        })

        self.assertTrue(form.is_valid())

    def test_new_user_form_no_data(self):
        form = NewUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)  # should have 4 fields with errors - username, email, password1, password2