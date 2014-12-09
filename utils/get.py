#!/usr/bin/python


import xml.etree.ElementTree as ET


def main():
    with open('csPaper', 'r') as csPaper:
        tree = ET.parse(csPaper)
        root = tree.getroot()
        for child in root:
            if child.tag.find('entry') > 1:
                for entry in child:
                    if entry.tag.find('summary') > 1:
                        print 'ABSTRACT_BEGIN'
                        print entry.text


if __name__ == "__main__":
    main()
