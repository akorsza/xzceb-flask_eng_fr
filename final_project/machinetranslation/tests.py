import unittest
from translator import english_to_french, french_to_english

class Test_translated(unittest.TestCase):
    def test_hello_e2f(self):
        text = 'Hello'
        translated_text = 'Bonjour'
        self.assertEqual(english_to_french(text),translated_text)
    def test_hello_f2e(self):
        text = 'Bonjour'
        translated_text = 'Hello'
        self.assertEqual(french_to_english(text),translated_text)
        