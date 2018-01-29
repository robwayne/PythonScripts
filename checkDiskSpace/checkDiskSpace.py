#!/usr/bin/pythonw

#Author: Robert Gordon
#Date: Jan 2, 2018

import os
import subprocess
import argparse

BYTES_PER_GIGABYTE = pow(10,9)
FREE_SPACE_THRESHOLD = 5

def check():
    args = getArgs()
    stat = os.statvfs('/')
    gbFree = (stat.f_bavail * stat.f_frsize)/BYTES_PER_GIGABYTE

    if gbFree <= FREE_SPACE_THRESHOLD and args.verbose:
        print("Remaining disk space is LOW (%.02f GB). System will be purged."%gbFree)
        subprocess.call(['purge.py', '-vv'])
    elif gbFree <= FREE_SPACE_THRESHOLD and not args.verbose:
        subprocess.call(['purge.py', '-vv'])
    elif gbFree > FREE_SPACE_THRESHOLD and args.verbose:
        print("System has adequate free disk space (%0.2f GB)."%gbFree)


def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-v","--verbose", help="Makes the output more verbose",action="store_true")
    args = parse.parse_args()
    return args


if __name__ == "__main__":
    check()
