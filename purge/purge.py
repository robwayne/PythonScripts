#!/usr/bin/env python3
import os
import shutil


def main():
    src = "/Users/robudhabi"
    directories = os.listdir(src)
    directories = getRelevantDirectories(directories)


def getRelevantDirectories(directories):
    relevantDirectories = ["Desktop", "Document", "Downloads"]
    for dir in directories:
        if dir[0]
if __name__ == "__main__":
    main()
