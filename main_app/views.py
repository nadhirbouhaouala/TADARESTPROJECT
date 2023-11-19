from django.shortcuts import render, redirect

from .models import *
from .forms import *

from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

data_base = 'offline_db'
object_name = 'Task'

def Logout():
    return redirect('Task_list')

def index(request):
    request.session['user'] = 'Nadhir'
    return render(request, "Pages/login.html")

def TaskList(request):
    object_list = Task.objects.all()
    request.session['user'] = 'Nadhir'
    context={'object_list':object_list,'object_name':object_name}
    return render(request , 'Task/list.html' , context)

def TaskDetail(request, pk):
    object = Task.objects.get(id=pk)
    request.session['user'] = 'Nadhir'
    context={'object':object,'object_name':object_name}
    return render(request , 'Task/detail.html' , context)

def TaskCreate(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save(commit=False).save()
                return redirect('Task_list')
            except:
                 pass
    request.session['user'] = 'Nadhir'
    context={'form':form,'object_name':object_name}
    return render(request , 'Task/form.html' , context)

def TaskUpdate(request, pk):
    object = Task.objects.get(id=pk)
    form = TaskForm(instance = object)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = object)
        if form.is_valid():
            try:
                form.save(commit=False).save()
                return redirect('Task_list')
            except:
                pass
    request.session['user'] = 'Nadhir'
    context={'form':form,'object_name':object_name}
    return render(request , 'Task/form.html' , context)

def TaskDelete(request, pk):
    object = Task.objects.get(id=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('Task_list')
    return render(request , 'Task/confirm_delete.html')

@api_view(['GET'])
def TaskListAPI(request):
    object_list = Task.objects.all()
    serializer = TaskSerializer(object_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreateAPI(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

