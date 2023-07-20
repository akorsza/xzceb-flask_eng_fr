from deep_translator import MyMemoryTranslator

#english_text = 'Hello world, welcome to python'
#french_text = 'Bonjour le monde, bienvenue en python'

#functions to translate text

def english_to_french(english_text):
    """
    Function to translate english text to french one
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Function to translate english text to french one
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text