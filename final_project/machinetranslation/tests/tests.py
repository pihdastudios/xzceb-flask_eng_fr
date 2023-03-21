import unittest
from translator import englishToFrench, frenchToEnglish

class Tests(unittest.TestCase):
    def testNullEnToFr(self):
        self.assertRaises(ValueError, englishToFrench, None)

    def testEnToFr(self):
        actual = englishToFrench("Hello")
        expected = "Bonjour"
        self.assertEqual(actual, expected)
        self.assertNotEqual(actual, "Hello")

    def testNullFrToEn(self):
        self.assertRaises(ValueError, frenchToEnglish, None)

    def testFrToEn(self):
        actual = frenchToEnglish("Bonjour")
        expected = "Hello"
        self.assertEqual(actual, expected)
        self.assertNotEqual(actual, "Bonjour")