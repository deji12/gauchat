from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from googletrans import Translator
translator = Translator()

def TextTrans(request):
    if request.method == 'POST':
        from_lang = request.POST.get('from_lang')
        to_lang = request.POST.get('to_lang')
        content = request.POST.get('content')

        if not from_lang:
            return HttpResponse('Specify conversion languages')

        if not to_lang:
            return HttpResponse('Specify conversion languages')

        translated = translator.translate(content, dest=f'{to_lang}', src=f'{from_lang}')
        return HttpResponse(translated.text)