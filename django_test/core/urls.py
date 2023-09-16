from django.urls import path

from . import views
from .views import MessageView

app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
    path("contact/", MessageView.as_view(), name='contact'),
    path("projects/", views.projects, name='projects'),
]