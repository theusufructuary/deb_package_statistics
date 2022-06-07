#!/usr/bin/python3

# Plan
# √ - import libs - urllib, argparse, gzip, logging (syslog)
# √ - receive command line arguments from user input using argparse
# √ - use urllib for http get request to Debian mirror to create a
#  local copy of Contents file of architecture requested by user
# √ - for loop to parse each line of the Contents file and count
# number of files associated with each package, storing results in an object
# √ - print names of the top 10 packages and the number of files
# associated with them, in descending order (largest printed first)
# √ - amend package names printed to screen
# - alignment of printed columns
# √ - implement basic logging to syslog
# √ - implement basic error handling (with try...except)
# - implement basic automated testing with unittest

import argparse
import urllib.request
import gzip
import syslog


def get_contents_file(args):
    try:
        return urllib.request.urlopen(
            'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{}.gz'
            .format(
                args.arch
            )
        )
    except ConnectionError:
        print('Cannot connect to Debian mirror')
        syslog.syslog(syslog.LOG_CRIT, 'Cannot connect to Debian mirror.')
        quit()
    except urllib.error.HTTPError:
        print('Architecture not found')
        quit()


def format_lines():

    counter = dict()

    for line in contents_dec:
        words = line.split()

        for word in words:
            index = word.find(b'/')
            wordReduced = word[index + 1:]
            counter[wordReduced] = counter.get(wordReduced, 0) + 1

    return counter


def sort_list():

    countedList = list()

    for key, value in counter.items():
        countedTup = (value, key)
        countedList.append(countedTup)

    sortedCountedList = sorted(countedList, reverse=True)

    for value, key in sortedCountedList[0:10]:
        print(f"{key}{value : >10}")


parser = argparse.ArgumentParser(description='Select an architecture')

parser.add_argument('arch', type=str, help='architecture')

args = parser.parse_args()

contents = get_contents_file(args)

contents_dec = gzip.open(contents)

counter = format_lines()

sort_list()
