#!/usr/bin/python

import textGeneratorBackend
import unittest


class TestNormalWorking(unittest.TestCase):
    def setUp(self):
        self.o = textGeneratorBackend.StatisticsTextGenerator(
            penalty=10, gramN=3, wordNum=9)

    def test_wordsWillBeRepeatedAfterExhaustion(self):
        self.assertEqual(
            self.o.generateText(['A', 'b', 'c', 'A', 'b', 'c']),
            ['A', 'b', 'c', 'A', 'b', 'c', 'A', 'b', 'c'])


class TestDegenerateCases(unittest.TestCase):
    def setUp(self):
        self.o = textGeneratorBackend.StatisticsTextGenerator(
            penalty=10, gramN=4, wordNum=1940)

    def test_tooFewWords(self):
        # What to do in this case?
        self.o.generateText(['A', 'b'])

if __name__ == '__main__':
    unittest.main()
