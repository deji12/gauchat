from django.urls import path
from lang_translate.views import TextTrans

urlpatterns =[
    path('translate-text/', TextTrans,name='translate'),    
]
