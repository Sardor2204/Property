import controlDB
from googletrans import Translator

translator = Translator()

def translate(id, text):
    lang = controlDB.control.language(id)

    if lang == 0:
        return text
    elif lang == 1:
        result = translator.translate(str(text), src='ru', dest='en')
    else:
        result = translator.translate(str(text), src='ru', dest='uz')

    return result.text


def antyTranslate(id, text):
    lang = controlDB.control.language(id)

    if lang == 0:
        return text
    elif lang == 1:
        result = translator.translate(str(text), src='en', dest='ru')
    else:
        result = translator.translate(str(text), src='uz', dest='ru')

    return result.text