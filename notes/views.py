from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Note
from django.http import HttpResponse, JsonResponse

# Create your views here.

@login_required
def AddNote(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        filter_notes = Note.objects.filter(title=request.POST.get('note_name'))
        if not filter_notes:
            new_note = Note(author=get_logged_in_user, title=request.POST.get('note_name'), content=request.POST.get('note_detail'), tag=request.POST.get('tag'))
            new_note.save()
            success = '| Note Added'
            return HttpResponse(success)
        else:
            success = '| Note Title Alerady Exists'
            return HttpResponse(success)

@login_required
def UpdateNote(request, name):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_note = Note.objects.get(div_name=name)
    if request.method == 'POST':
        if request.POST.get('tag_name') == 'delete':
            get_note.delete()
            success = '| Note Deleted'
            return HttpResponse(success)
        else:
            print(name)
            get_note_for_update = Note.objects.get(div_name=name)
            get_note_for_update.tag = request.POST.get('tag_name')
            get_note_for_update.save()
            success = '| Note Updated'
            return HttpResponse(success)

@login_required
def get_notes(request):
    if request.method == 'POST':
        if request.POST.get('status') == 'All Notes':
            get_note = Note.objects.filter(author=request.user)
            return JsonResponse({"notes":list(get_note.values())})
          
        elif request.POST.get('status') == 'Personal':
            get_note = Note.objects.filter(author=request.user)
            return JsonResponse({"notes":list(get_note.values())})

        elif request.POST.get('status') == 'Work':
            get_note = Note.objects.filter(author=request.user, tag='Work')
            return JsonResponse({"notes":list(get_note.values())})

        elif request.POST.get('status') == 'Favourite':
            get_note = Note.objects.filter(author=request.user, tag='Favourite')
            return JsonResponse({"notes":list(get_note.values())})

        elif request.POST.get('status') == 'Important':
            get_note = Note.objects.filter(author=request.user, tag='Important')
            return JsonResponse({"notes":list(get_note.values())})
    else:
        pass

def search(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    # get_logged_in_users_task = Task.objects.filter(user=get_logged_in_user)
    if request.method == 'POST':
        print('yesssssssssssp----------------------------')
        search_val = request.POST.get('search')
        get_note = Note.objects.filter(title__contains=search_val)
        # context = {
        #     'profile': get_logged_in_users_profile,
        #     'task': get_task,
        #     'date': dates,
        # }
        return JsonResponse({"notes":list(get_note.values())})


    
        
        