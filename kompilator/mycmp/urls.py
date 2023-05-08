from django.urls import path

from . import views

urlpatterns = [
    path('', views.awww1, name='aww1'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('add_directory/', views.add_directory, name='add_directory'),
    path('delete_directory/', views.delete_directory, name='delete_directory'),
    path('show_file_content/', views.show_file_content, name='show_file_content'),
    path('delete_file/', views.delete_file, name='delete_file'),
    path('runcode/', views.runcode, name='runcode'),
]