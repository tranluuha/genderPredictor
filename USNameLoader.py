#!/usr/bin/env python
# encoding: utf-8
"""
USNameLoader.py
"""
import re

def _getNameList(filename):
    regex = '([A-Z]+) +([0-9\.]+) +([0-9\.]+) +([0-9]+)'

    names = list()
    namesFile = open(filename, 'rb')
    for row in namesFile.readlines():
        row = re.search(regex,row).groups()

        names.append(
            (row[0],float(row[1]),float(row[2]),int(row[3]))
            )
        
    return names
        
def getNameList():
    maleNames = _getNameList('dist.male.first.first')
    femaleNames = _getNameList('dist.female.first.first')
    
    return (maleNames,femaleNames)
if __name__ == "__main__":
    print getNameList()