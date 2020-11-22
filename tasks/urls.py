from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_tasks, name='show_tasks'),
    path('', views.create_tasks, name='create_tasks'),
]
