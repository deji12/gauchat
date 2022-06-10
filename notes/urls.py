from django.urls import path
from . import views

urlpatterns = [
    path('add-note/', views.AddNote, name='add-note'),
    path('update-note/<str:name>/', views.UpdateNote, name='update-note'),
    path('get-notes/', views.get_notes, name='get-notes'),
    path('search-note/', views.search, name='search-note'),
]