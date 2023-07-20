import unittest
from translator import english_to_french, french_to_english

#Unit tests for the created translator functions:
class Test_translated(unittest.TestCase):
    def test_e2f_equal(self):
        text = 'Hello'
        translated_text = 'Bonjour'
        self.assertEqual(english_to_french(text),translated_text)

    def test_e2f_not_equal(self):
        text = 'Hello'
        self.assertNotEqual(english_to_french(text),'Hello')

    def test_f2e_equal(self):
        text = 'Bonjour'
        translated_text = 'Hello'
        self.assertEqual(french_to_english(text),translated_text)
    def test_f2e_not_equal(self):
        text = 'Bonjour'
        self.assertNotEqual(french_to_english(text),'Bonjour')

if __name__ == '__main__':
    unittest.main()