import unittest

from translator import english_to_french, french_to_english

class TestTranslators(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()