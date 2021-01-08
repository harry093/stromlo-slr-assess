#!/usr/bin/env python3

""" Code to perform the Mt Stromlo SLR monthly assessment

The codes that we have been using for the DORs for a long time are;

1 – Data OK
2 – not used
3 – No returns (justified)
4 – No returns(not justified)
5 – No attempt (justified)
6 – No attempt (not justified)

A – Aircraft detected
C – Predictions degraded
D – Low elevation
E – Miscellaneous (rarely used)
F – Equipment malfunction
L – Sun affected
M – Site restrictions
P – Priority conflict
U – Upgrade/maintenance
X – Unknown
Z – Weather

We have other codes, H, I and W that are never used.

"""



"""
Old stuff

import re
import datetime
from dateutil.relativedelta import relativedelta
import os

# Compile a regular expression that matches a DOR filename
p = re.compile(r"dor\d{3}.txt")

# Get the month/year being assessed and check all DOR files are present
year = datetime.date.today().year
first = True
filenames = os.listdir("dor_files")
for file in sorted(filenames):
    if p.match(file):
        doy = file[3:6]
        date = datetime.datetime.strptime(str(year) + ' ' + doy, '%Y %j')
        if first:
            first_day = date
            last_day = first_day + relativedelta(months=1) - \
                datetime.timedelta(days=1)
            print(first_day, last_day)
            num_days = last_day - first_day + 1
            print(num_days)
            month = date.month
            if date.day != 1:
                print('ooops')
            first = False

seen = {}
dupLines = set()
dorFiles = {}
tlrBlock = set()
slrBlock = set()
duplicates = []

# T < -27 clear; T > -27 cloudy

    lines = []
    go = False
    for line in open('dor_files/' + file):
        line = line.rstrip()
        if go and line[0:4] == '----':
            break
        if go:
            lines.append(line)
        if line[0:4] == '----':
            go = True
    doSLR = False
    for line in lines:
        try:
            dorFiles[line].add(file)
        except KeyError:
            dorFiles[line] = set()
            dorFiles[line].add(file)
        if line == '':
            doSLR = True
        if line != '':
            if line not in seen:
                seen[line] = 1
            else:
                dupLines.add(line)
                seen[line] += 1
            if doSLR:
                slrBlock.add(line)
            else:
                tlrBlock.add(line)

for dupLine in dupLines:
    duplicates.append([seen[dupLine], dupLine, dorFiles[dupLine]])
duplicates.sort(key=lambda x: x[1])

for dup in duplicates:
    print('{:3d} {}   {}'.format(dup[0], dup[1], dup[2]))

print(len(slrBlock))
print(len(tlrBlock))

"""
