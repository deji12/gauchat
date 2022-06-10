from telnetlib import STATUS
from django.shortcuts import render
from .models import Task, task_date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from datetime import date
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def add_task(request):
    new_task_date = task_date.objects.filter(date=date.today(), user=request.user)
    get_logged_in_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        filter_task = Task.objects.filter(task_name=request.POST.get('task_name'))
        if not filter_task:
            if new_task_date:
                new_task = Task(task_name= request.POST.get('task_name'), task_detail = request.POST.get('task_detail'), user=get_logged_in_user, parent_date = task_date.objects.get(date=date.today(), user=request.user))
                new_task.save()
                success = '| Task Added'
                return HttpResponse(success)
            else:
                new_date = task_date(user=request.user, date=date.today())
                new_date.save()
                new_task = Task(task_name= request.POST.get('task_name'), task_detail = request.POST.get('task_detail'), user=get_logged_in_user, parent_date = new_date)
                new_task.save()
                success = '| Task Added'
                return HttpResponse(success)
        else:
            success = '| Task Alerady Exists'
            return HttpResponse(success)

@login_required
@csrf_exempt
def update_task_finished(request, name):
    if request.method == 'POST':
        get_logged_in_user = User.objects.get(username=request.user.username)
        get_task_by_name = Task.objects.get(task_name=name)
        get_task_by_name.status = True
        get_task_by_name.save()

        get_task_for_logged_in_user = Task.objects.filter(user=get_logged_in_user)
    
        return HttpResponse('| Task Updated')

@login_required
def update_task_content(request, name):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_task_by_name = Task.objects.get(user=get_logged_in_user, task_name=name)
    if request.method == 'POST':
        if request.POST.get('task_name'):
            get_task_by_name.task_name = request.POST.get('task_name')
            get_task_by_name.save()
        if request.POST.get('task_detail'):
            get_task_by_name.task_detail = request.POST.get('task_detail')
            get_task_by_name.save()
        return HttpResponse('TaskUpdated')


@login_required
def get_tasks(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    todos = Task.objects.filter(user=get_logged_in_user)
    return JsonResponse({"todos":list(todos.values())})
