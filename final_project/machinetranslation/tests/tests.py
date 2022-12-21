import sys
sys.path.append('/home/project/xzceb-flask_eng_fr/final_project')
import unittest
from machinetranslation import translator

class TestTranslationMethods(unittest.TestCase):
    def test_englishToFrenchNone(self):
        input_text = None
        self.assertIsNone(translator.english_to_french(input_text))

    def test_frenchToEnglishNone(self):
        input_text = None
        self.assertIsNone(translator.french_to_english(input_text))

    def test_englishToFrenchHello(self):
        input_text = "Hello"
        expected_output = "Bonjour"
        self.assertEqual(translator.english_to_french(input_text), expected_output)

    def test_frenchToEnglishBonjour(self):
        # Prueba de traducción del francés al inglés con una cadena de texto sencilla
        input_text = "Bonjour"
        expected_output = "Hello"
        self.assertEqual(translator.french_to_english(input_text), expected_output)


if __name__ == '__main__':
    unittest.main()