#!/usr/bin/python

import codecs
from sys import stderr
import textGeneratorBackend


def createWordlist(fileName):
    f = codecs.open(fileName, 'r', "utf-8")
    wordList = []
    for line in f:
        for word in line.strip().split(' '):
            if word not in [u'', u'-']:
                wordList.append(word+u' ')
    return wordList


def writeList(fileName, finalList):
    out = codecs.open(fileName, 'w', 'utf-8')
    for w in finalList:
        out.write(w)
    out.write('\n')


def main():
    wo = createWordlist('text/edesAnna')
    w = []
    character = True
    if character:
        for wi in wo:
            for wj in wi:
                w.append(wj)
    else:
        w = wo
    o = textGeneratorBackend.StatisticsTextGenerator(
        penalty=10, gramN=4, wordNum=1940)
    writeList('edesAnna.genText', o.generateText(w))


if __name__ == "__main__":
    main()
