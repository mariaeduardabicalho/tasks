from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.


def index(request):
	return HttpResponse("Hello, world. You're at the tasks index.")


def show_tasks(request): 
	task= Task.objects.all()
	# serializer_class = TaskSerializer
	jsontask = serializers.serialize("json", task)
	return HttpResponse(jsontask,content_type="application/json")

from django.shortcuts import render 

# Create your views here. 
def create_tasks(request): 
	data = JSONParser().parse(request)
	serializer = TaskSerializer(data=data)

	if serializer.is_valid():
		serializer.save()
		return HttpResponse(serializer.data, status=201)
	return HttpResponse(serializer.errors, status=400)


