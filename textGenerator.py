#!/usr/bin/python

import argparse
import codecs
from sys import stdout
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
    out = stdout
    if fileName != '_SDTOUT_':
        out = codecs.open(fileName, 'w', 'utf-8')
    for w in finalList:
        out.write(w)
    out.write('\n')


def main():
    parser = argparse.ArgumentParser(description='In this paper, we...')
    parser.add_argument("-c", "--character", action="store_true",
                        help='Process text on character level')
    parser.add_argument("-p", "--penalty", type=int, default=10)
    parser.add_argument("-n", "--gramN", type=int, default=3)
    parser.add_argument("-w", "--wordNum", type=int, default=60)
    parser.add_argument("inputFile")
    parser.add_argument("-o", "--outFile", type=str, default='_SDTOUT_',
                        help='stdout is used if not given specified')
    args = parser.parse_args()

    wo = createWordlist(args.inputFile)
    w = []
    if args.character:
        for wi in wo:
            for wj in wi:
                w.append(wj)
    else:
        w = wo
    o = textGeneratorBackend.StatisticsTextGenerator(
        penalty=args.penalty, gramN=args.gramN, wordNum=args.wordNum)
    writeList(args.outFile, o.generateText(w))


if __name__ == "__main__":
    main()
