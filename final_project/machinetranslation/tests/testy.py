import unittest
from translator import englishToFrench, frenchToEnglish

class Test_translated(unittest.TestCase):
    def test_hello_e2f(self):
        text = 'Hello'
        translated_text = 'Bonjour'
        self.assertEqual(englishToFrench(text),translated_text)
    def test_hello_f2e(self):
        text = 'Bonjour'
        translated_text = 'Hello'
        self.assertEqual(frenchToEnglish(text),translated_text)
        