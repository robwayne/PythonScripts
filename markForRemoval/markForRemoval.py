#!/usr/bin/env python3

''' A script to work in tandem with purge.py. Renames all the files in certain directories to either
        "delete_<file/folder_name>" or "keep_<file_name>" '''

import os
import argparse
import sys

protectedFolders = ["Desktop","Downloads", ".Trash"]

def main():
    args = getArgs()
    method = args.method

    if method == "mark" or method is None:
        if args.path is None:
            markForRemoval()
        else:
            markForRemoval(root=args.path)
    elif method == "unmark":
        if args.path is None:
            unmark()
        else:
            unmark(root=args.path)

def markForRemoval(**path):
    toplevelDirectory = os.getcwd()

    if ('root' in path):
        currentDir = path['root']
        walkTree(currentDir)
    else:
        for folder in protectedFolders:
            currentDir = os.path.join(toplevelDirectory,folder)
            os.chdir(currentDir)
            walkTree(currentDir)


def walkTree(directoryPath):
    tempName = ""
    prefix = "delete_"
    script = sys.argv[0] #get the name of the script being ran
    if script.startswith("./"): #if the user entered './rename.py' to run it, remove the './'
        script = script[2:]

    for dpath, dirs, files in os.walk(directoryPath, topdown=False):
        print(dpath)
        print(dirs)
        print(files)
        os.chdir(dpath)
        for directory in dirs:
            if ( (directory not in protectedFolders) and (not directory.startswith("keep_")) ):
                if not directory.startswith("delete_"):
                    tempName = prefix+directory
                    print(tempName)
                    os.rename(directory,tempName)
        for filename in files:
            if not filename.startswith("delete_") and not filename.startswith("keep_"):
                if filename != script:
                    #print(filename)
                    tempName = prefix+filename
                    print(tempName)
                    os.rename(filename,tempName)

def unmark(**path):
    if 'root' in path:
        currentDir = path['root']
    else:
        currentDir = os.getcwd()

    print(currentDir)

    for dpath, dirs, files in os.walk(currentDir, topdown=False):
        os.chdir(dpath)
        print(dpath)
        print(dirs)
        print(files)
        for directory in dirs:
            if directory.startswith("delete_"):
                print(directory[7:])
                os.rename(directory, directory[7:])
        for filename in files:
            if filename.startswith("delete_"):
                print(filename[7:])
                os.rename(filename,filename[7:])


def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-m", "--method", help="the name of the task to perform: 'mark' to label the items to be deleted or remove the \
        label that was set previously", choices=["mark","unmark"])
    parse.add_argument("-p","--path",help="The path to the root directory of the tree to rename the files and folders from")
    args = parse.parse_args()
    return args

if __name__ == "__main__":
    main()
else:
    print(protectedFolders)
