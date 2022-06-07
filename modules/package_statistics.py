#!/usr/bin/python3

# Plan
# - import libs - urllib, argparse, requests, gzip, logger
# √ - receive command line arguments from user input using argparse
# - use urllib for http get request to Debian mirror to create a
#  local copy of Contents file of architecture requested by user
# - for loop to parse each line of the Contents file and count
# number of files associated with each package, storing results in an object
# - print names of the top 10 packages and the number of files
# associated with them, in descending order (largest printed first)


import argparse


parser = argparse.ArgumentParser(description='Select an architecture')
parser.add_argument('arch', type=str, help='architecture')

args = parser.parse_args()
print(vars(args))
