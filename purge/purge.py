#!/usr/bin/env python3

import os
import shutil
import argparse


def main():
    args = getArgs()
    src = args.root
    directories = os.listdir(src)
    print(directories)
    directories = getRelevantDirectories(directories)


def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("root",help="the root directory to purge children tree")
    args = parse.parse_args()
    return args

def getRelevantDirectories(directories):
    relevantDirectories = ["Desktop", "Document", "Downloads"]


if __name__ == "__main__":
    main()
