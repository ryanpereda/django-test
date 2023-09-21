from django.urls import path

from . import views
from .views import MessageView

app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
    path("contact/", views.contact, name='contact'),
    path("projects/", views.projects, name='projects'),
]