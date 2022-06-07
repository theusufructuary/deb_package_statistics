#!/usr/bin/python3

# Plan
# - import libs - urllib, argparse, gzip, logger
# √ - receive command line arguments from user input using argparse
# √ - use urllib for http get request to Debian mirror to create a
#  local copy of Contents file of architecture requested by user
# √ - for loop to parse each line of the Contents file and count
# number of files associated with each package, storing results in an object
# √ - print names of the top 10 packages and the number of files
# associated with them, in descending order (largest printed first)
# √ - amend package names printed to screen
# - alignment of counted items
# - implement basic logging
# √ - implement basic error handling
# - implement basic testing

import argparse
import urllib.request
import gzip

parser = argparse.ArgumentParser(description='Select an architecture')
parser.add_argument('arch', type=str, help='architecture')

args = parser.parse_args()


try:
    contents = urllib.request.urlopen(
        'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{}.gz'.format(
            args.arch
        )
    )
except:
    print('Could not reach mirror.')
    quit()


contents_dec = gzip.open(contents)


counter = dict()

for line in contents_dec:
    words = line.split()

    for word in words:
        index = word.find(b'/')
        wordReduced = word[index + 1:]
        counter[wordReduced] = counter.get(wordReduced, 0) + 1


countedList = list()

for key, value in counter.items():
    countedTup = (value, key)
    countedList.append(countedTup)

sortedCountedList = sorted(countedList, reverse=True)

for value, key in sortedCountedList[0:10]:
    print(f"{key}{value : >10}")
