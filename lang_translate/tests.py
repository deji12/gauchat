from django.test import TestCase

# Create your tests here.
from googletrans import Translator
translator = Translator()

from_lang = 'en'
to_lang = 'tr'
content = 'i am a boy'

translated = translator.translate(content, dest=f'{to_lang}', src=f'{from_lang}')
print(translated.text)