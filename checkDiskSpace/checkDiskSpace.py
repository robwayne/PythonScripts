#!/usr/bin/env python3.5

#Author: Robert Gordon
#Date: Jan 2, 2018

import os
import subprocess

BYTES_PER_GIGABYTE = pow(10,9)
FREE_SPACE_THRESHOLD = 5

def check():
    stat = os.statvfs('/')
    gbFree = (stat.f_bavail * stat.f_frsize)/BYTES_PER_GIGABYTE

    if gbFree <= FREE_SPACE_THRESHOLD:
        subprocess.call(['purge.py', '-vv'])


if __name__ == "__main__":
    check()
