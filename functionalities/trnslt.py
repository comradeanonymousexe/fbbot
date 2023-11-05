from translate import Translator

def translate_arabic_to_english(text):
    translator = Translator(to_lang="en", from_lang="ar")
    translation = translator.translate(text)
    return translation

def translate_english_to_arabic(text):
    translator = Translator(to_lang="ar", from_lang="en")
    translation = translator.translate(text)
    return translation
