from deep_translator import MyMemoryTranslator
def english_to_french(englishText):
    translator = MyMemoryTranslator(source='en', target = 'fr')
    frenchText = translator.translate(englishText)
    return frenchText
def french_to_english(frenchText):
    translator = MyMemoryTranslator(source='fr', target = 'en')
    englishText = translator.translate(frenchText)
    return englishText