from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
    path('pdf/<int:pdf_id>/', views.pdf_view, name='pdf_view'),
    path("projects/", views.projects, name='projects'),
    # path("contact/", views.contact, name='contact'),
]