"""notestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import NoteListCreate, NoteGetUpdateDelete
from users.views import UserRegistrationView, UserListView, UserGetUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteGetUpdateDelete.as_view(), name='note-get-update-delete'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserGetUpdate.as_view(), name='user-get-update-delete')
]
