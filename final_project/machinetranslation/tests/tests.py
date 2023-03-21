import unittest
from translator import englishToFrench, frenchToEnglish

class Tests(unittest.TestCase):
    def testNullEnToFr(self):
        englishToFrench(None)

    def testNullFrToEn(self):
        frenchToEnglish(None)

    def testEnToFr(self):
        actual = englishToFrench("Hello")['translations'][0]['translation']
        expected = "Bonjour"
        self.assertEqual(actual, expected)

    def testFrToEn(self):
        actual = frenchToEnglish("Bonjour")['translations'][0]['translation']
        expected = "Hello"
        self.assertEqual(actual, expected)