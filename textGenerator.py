#!/usr/bin/python

import codecs
from sys import stderr
from collections import defaultdict
from heapq import heappush, heappop


class StatisticsTextGenerator(object):
    def __init__(self, gramN=2, penalty=3, wordNum=120):
        self.gramN = gramN
        self.penalty = penalty
        self.wordNum = wordNum
        self.nGrams = defaultdict(lambda: defaultdict(int))

    def createNgram(self):
        for i in range(len(self.wordList)-self.gramN):
            first = tuple(self.wordList[i:i+self.gramN-1])
            follow = self.wordList[i+self.gramN-1]
            self.nGrams[first][follow] += 1

    def createDict(self):
        result = defaultdict(list)
        maxKeys = []
        for key, value in self.nGrams.iteritems():
            sumV = 0
            for k, v in value.iteritems():
                heappush(result[key], (-v, k))
                sumV += v
            heappush(maxKeys, (-sumV, key))
        return result, maxKeys

    def generateText(self, wordList):
        self.wordList = wordList
        self.createNgram()
        nGramDict, maxKeys = self.createDict()
        result = []
        t = maxKeys[:]
        while not t[0][1][0].isupper():
            heappop(t)
        result = list(t[0][1])
        for _ in range(self.wordNum):
            p = tuple(result[-self.gramN+1:])
            popped = heappop(nGramDict[p])
            result.append(popped[1])
            heappush(nGramDict[p], (popped[0] + self.penalty, popped[1]))
        return result


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
        if u'ABSTRACT_BEGIN ' == w:
            out.write('\n\n')
        out.write(w)
    out.write('\n')


def main():
    wo = createWordlist('text/csPaper.txt')
    w = []
    character = False
    if character:
        for wi in wo:
            for wj in wi:
                w.append(wj)
    else:
        w = wo
    o = StatisticsTextGenerator(penalty=10, gramN=4, wordNum=3340)
    writeList('csPaper.genText', o.generateText(w))


if __name__ == "__main__":
    main()
