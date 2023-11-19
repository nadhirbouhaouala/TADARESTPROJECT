from django.urls import path
from .views import *

urlpatterns = [
    #path('', index),

    path('Logout', Logout),

    path('Task', TaskList, name='Task_list'),
    path('Task/view/<int:pk>', TaskDetail, name='Task_view'),
    path('Task/new', TaskCreate, name='Task_new'),
    path('Task/edit/<int:pk>', TaskUpdate, name='Task_edit'),
    path('Task/delete/<int:pk>', TaskDelete, name='Task_delete'),

    path('TaskAPI', TaskListAPI),
    path('TaskAPI/new', TaskCreateAPI),

]