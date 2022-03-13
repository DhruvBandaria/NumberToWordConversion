import unittest
from main import getWordNumber


class NumberToWordTestCase(unittest.TestCase):

    def testNumber1(self):
        result = getWordNumber(298765)
        self.assertEqual(result, r'Two Hundred Ninety Eight Thousand Seven Hundred Sixty Five ')

    def testNumber2(self):
        result = getWordNumber(100)
        self.assertEqual(result, "One Hundred ")

    def testNumber3(self):
        result = getWordNumber(321)
        self.assertEqual(result, "Three Hundred Twenty One ")

    def testNumber4(self):
        result = getWordNumber(21)
        self.assertEqual(result, "Twenty One ")

