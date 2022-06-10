from django.urls import path
from . import views

urlpatterns = [
    path('add-task/', views.add_task, name='add-task'),
    path('update-task/<str:name>/', views.update_task_content,name='update-task'),
    path('update-task/finished/<str:name>/', views.update_task_finished,name='update-task-finished'),
    path('get-tasks/', views.get_tasks, name='get-tasks')
]