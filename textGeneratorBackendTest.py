#!/usr/bin/python

import textGeneratorBackend
import unittest


class TestNormalWorking(unittest.TestCase):
    def setUp(self):
        self.o = textGeneratorBackend.StatisticsTextGenerator(
            penalty=10, gramN=3, wordNum=18)

    def test_wordsWillBeRepeatedAfterExhaustion(self):
        self.assertEqual(
            self.o.generateText(['A', 'b', 'c', 'A', 'b']),
            ['A', 'b', 'c', 'A', 'b', 'c', 'A', 'b', 'c',
             'A', 'b', 'c', 'A', 'b', 'c', 'A', 'b', 'c'])

    def test_wordIsChoosenFromListWhenNoNgrmaIsAvaliable(self):
        # Note: this came from the actual result.
        self.assertEqual(
            self.o.generateText(['A', 'b', 'c']),
            ['A', 'b', 'c', 'b', 'c', 'A', 'b', 'c',
             'A', 'b', 'c', 'A', 'b', 'c', 'A', 'b', 'c', 'A'])


class TestDegenerateCases(unittest.TestCase):
    def setUp(self):
        self.o = textGeneratorBackend.StatisticsTextGenerator(
            penalty=10, gramN=4, wordNum=1940)

    def test_tooFewWords(self):
        # What to do in this case?
        self.assertEqual(
            self.o.generateText(['A', 'b']),
            [])

if __name__ == '__main__':
    unittest.main()
