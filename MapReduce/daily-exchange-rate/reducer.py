#!/usr/bin/python
# The Mapper
import sys
import csv
# Set local variables
iteration = 0
currentCountry = None
previousCountry = None
currentFx = None
previousFx = None
percentChange = None
currentKey = None
fxMap = []

infile = sys.stdin
next(infile) 
for line in infile:
line = line.strip()
    line = line.split(',', 2)
try:

        currentCountry = line[1].rstrip()
        if len(line[2]) == 0:
            continue
        currentFx = float(line[2])
if currentCountry != previousCountry:
            previousCountry = currentCountry
            previousFx = currentFx
            previousLine = line
            continue
If country same as previous, add to map
        elif currentCountry == previousCountry:
            percentChange = ((currentFx - previousFx) / previousFx) * 100.00
            percentChange = round(percentChange, 2)
            percentChange = percentChange
currentKey = "%s: %6.2f%%" % (currentCountry, percentChange)

            fxMap.append(tuple([currentKey, 1]))

        previousCountry = currentCountry
        previousFx = currentFx
        previousLine = line

    except Exception as e:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print "currentFx: %.2f previousFx: %.2f" % (currentFx, previousFx)
        print message
        sys.exit(0)

for i in sorted(fxMap):
    print "%-20s - %d" % (i[0], i[1])