#!/usr/bin/python3

# Plan
# - import libs - urllib, argparse, requests, gzip, logger
# √ - receive command line arguments from user input using argparse
# √ - use urllib for http get request to Debian mirror to create a
#  local copy of Contents file of architecture requested by user
# - for loop to parse each line of the Contents file and count
# number of files associated with each package, storing results in an object
    # use split() to split first from second word on each line
# - print names of the top 10 packages and the number of files
# associated with them, in descending order (largest printed first)

import argparse
import urllib
import requests
import gzip

parser = argparse.ArgumentParser(description='Select an architecture')
parser.add_argument('arch', type=str, help='architecture')

args = parser.parse_args()
# print('args:', vars(args))


contents = urllib.request.urlopen('http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{}.gz'.format(args.arch))

contents_dec = gzip.open(contents)

print(contents_dec.read(200))
