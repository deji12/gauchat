from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('register/', views.signup, name='register'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('account-update/', views.account_update,  name='update-account'),
    path('social-update',views.social_media_profiles, name='social-update'),
    path('change-password',views.password_change, name='password-change'),
    path('update-privacy', views.update_privacy,  name='update-privacy'),
    path('update-security', views.update_security, name='update-security'),
    path('search/', views.search, name='search'),
    path('filter-task/', views.filter_task, name='filter-task'),
]