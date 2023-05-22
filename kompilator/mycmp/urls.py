from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
from .views import CustomLogoutView, register_request

urlpatterns = [
    path('', views.awww1, name='aww1'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('add_directory/', views.add_directory, name='add_directory'),
    path('delete_directory/', views.delete_directory, name='delete_directory'),
    path('delete_file/', views.delete_file, name='delete_file'),
    path('runcode/', views.runcode, name='runcode'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("register/", register_request, name="register"),
    path('file_list_json/', views.file_list_json, name='file_list_json'),
    path('directory_list_json', views.directory_list_json, name='directory_list_json'),
]