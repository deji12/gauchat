from django import http
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todoblog.models import Task,task_date
from notes.models import Note

# Create your views here.

def home(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_logged_in_users_profile = Profile.objects.get(user=get_logged_in_user)
    get_logged_in_users_task = Task.objects.filter(user=get_logged_in_user)
    dates = task_date.objects.filter(user=request.user)
    notes = Note.objects.filter(author=get_logged_in_user).order_by('-date')
    context = {
        'profile': get_logged_in_users_profile,
        'task': get_logged_in_users_task,
        'date': dates,
        'notes': notes,
    }
    return render(request, 'chatapp/index.html', context)

def search(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_logged_in_users_profile = Profile.objects.get(user=get_logged_in_user)
    # get_logged_in_users_task = Task.objects.filter(user=get_logged_in_user)
    if request.method == 'POST':
        print('yesssssssssssp----------------------------')
        search_val = request.POST.get('search')
        get_task = Task.objects.filter(task_name__contains=search_val)
        print(get_task)
        dates = task_date.objects.filter(user=request.user)
        # context = {
        #     'profile': get_logged_in_users_profile,
        #     'task': get_task,
        #     'date': dates,
        # }
        return JsonResponse({"task":list(get_task.values())})

def filter_task(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        if request.POST.get('status') == 'All Tasks':
            get_task = Task.objects.filter(user=request.user)
            return JsonResponse({"task":list(get_task.values())})
          
        elif request.POST.get('status') == 'Active':
            get_task = Task.objects.filter(user=request.user, status=False)
            return JsonResponse({"task":list(get_task.values())})

        elif request.POST.get('status') == 'Finished':
            get_task = Task.objects.filter(user=request.user, status=True)
            return JsonResponse({"task":list(get_task.values())})
    else:
        pass


@csrf_exempt
def account_update(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_logged_in_users_profile = Profile.objects.get(user=get_logged_in_user)

    if request.method == 'POST':
        if request.POST.get('first_name'):
           get_logged_in_user.first_name = request.POST.get('first_name')
           get_logged_in_user.save()
        
        if request.POST.get('last_name'):
            get_logged_in_user.last_name = request.POST.get('last_name')
            get_logged_in_user.save()

        if request.POST.get('email'):
            get_logged_in_user.email = request.POST.get('email')
            get_logged_in_user.save()

        if request.POST.get('dob'):
            get_logged_in_users_profile.dob = request.POST.get('dob')
            get_logged_in_users_profile.save()

        if request.POST.get('number'):
           get_logged_in_users_profile.number = request.POST.get('number')
           get_logged_in_users_profile.save()

        if request.POST.get('address'):
            get_logged_in_users_profile.address = request.POST.get('address')
            get_logged_in_users_profile.save()

        if request.POST.get('website'):
            get_logged_in_users_profile.website = request.POST.get('website')
            get_logged_in_users_profile.save()

        if request.FILES.get('picture'):
            print('------------------------------------')
            get_logged_in_users_profile.picture = request.FILES.get('picture')
            get_logged_in_users_profile.save()


        success = 'Profile Updated Successfully'
        return HttpResponse(success)

def social_media_profiles(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_logged_in_users_profile = Profile.objects.get(user=get_logged_in_user)
    if request.method == 'POST':
        if request.POST.get('facebook'):
            get_logged_in_users_profile.facebook = request.POST.get('facebook')
            get_logged_in_users_profile.save()
        
        if request.POST.get('twitter'):
            get_logged_in_users_profile.twitter = request.POST.get('twitter')
            get_logged_in_users_profile.save()

        if request.POST.get('instagram'):
            get_logged_in_users_profile.instagram = request.POST.get('instagram')
            get_logged_in_users_profile.save()

        if request.POST.get('linkedin'):
            get_logged_in_users_profile.linkedin = request.POST.get('linkedin')
            get_logged_in_users_profile.save()

        success = 'Profile Updated Successfully'
        return HttpResponse(success)

#password change view
def password_change(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        if len(request.POST['confirm']) < 5:
            success = 'Password cannot be less than 5 characters'
            return HttpResponse(success)
        auth_user = authenticate(username=request.user.username, password=request.POST['old'])
        if auth_user is not None:
            if request.POST['new'] != request.POST['confirm']:
                success = 'Passwords do not match'
                return HttpResponse(success)
            else:
                get_logged_in_user.set_password(request.POST['confirm'])
                get_logged_in_user.save()
                logout(request)
                messages.success(request, 'Password changed successfully, login')
                success = 'Password changed successfully, login'
                return HttpResponse('{% url "login" %}')
        else:
            success = 'You have entered a wrong password'
            return HttpResponse(success)

def update_privacy(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_logged_in_users_profile = Profile.objects.get(user=get_logged_in_user)
    if request.method == 'POST':
        if request.POST.get('picture_see'):
            if request.POST.get('picture_see') == 'Friends':
                get_logged_in_users_profile.view_profile_pic = True
                get_logged_in_users_profile.save()
            elif request.POST.get('picture_see') == 'Public':
                get_logged_in_users_profile.view_profile_pic = False
                get_logged_in_users_profile.save()
    
        if request.POST.get('last_seen'):
            if request.POST.get('last_seen') == 'Friends':
                get_logged_in_users_profile.last_seen = True
                get_logged_in_users_profile.save()
            elif request.POST.get('last_seen') == 'Public':
                get_logged_in_users_profile.last_seen = False
                get_logged_in_users_profile.save()

        if request.POST.get('group'):
            if request.POST.get('group') == 'Friends':
                get_logged_in_users_profile.group = True
                get_logged_in_users_profile.save()
            elif request.POST.get('group') == 'Public':
                get_logged_in_users_profile.group = False
                get_logged_in_users_profile.save()

        success = 'Profile Updated Successfully'
        return HttpResponse(success)

def update_security(request):
    get_logged_in_user = User.objects.get(username=request.user.username)
    get_logged_in_users_profile = Profile.objects.get(user=get_logged_in_user)
    if request.method == 'POST':
        if request.POST.get('twofac'):
            if request.POST.get('twofac') == 'on':
                get_logged_in_users_profile.two_factor = True
                get_logged_in_users_profile.save()
            else:
                get_logged_in_users_profile.two_factor = False
                get_logged_in_users_profile.save()

        if request.POST.get('device'):
            if request.POST.get('device') == 'on':
                get_logged_in_users_profile.logged_in_device_setting = True
                get_logged_in_users_profile.save()
            else:
                get_logged_in_users_profile.logged_in_device_setting = False
                get_logged_in_users_profile.save()

        success = 'Profile Updated Successfully'
        return HttpResponse(success)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #validation before creating user
        if len(password) < 5:
            messages.error(request, 'Password cannot be less than 5 characters')
            return redirect('register')

        check_if_username_exists = User.objects.filter(username=username)
        if check_if_username_exists:
            messages.error(request, 'Username already exists, try another')
            return redirect('register')
        
        check_if_email_exist = User.objects.filter(email=email)
        if check_if_email_exist:
            messages.error(request, 'Email already exists, try another')
            return redirect('register')

        #create users
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        new_profile = Profile(user=new_user)
        new_profile.save()
        messages.success(request, 'User successfully creeated, proceed to login.')
        return redirect('login')
        
    return render(request, 'chatapp/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate user
        my_user = authenticate(username=username, password=password)
        if my_user is not None:
            login(request, my_user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong user details or user does not exist')
            return redirect('login')

    return render(request, 'chatapp/signin.html')

def logoutview(request):
    logout(request)
    return redirect('login')

def reset_password(request):
    return render(request, 'chatapp/reset-password.html')
