from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_tasks,'show_tasks'),
    path('', views.create_tasks,'create_tasks'),
]
