#!/usr/bin/env python3

''' A script to work in tandem with purge.py. Renames all the files in certain directories to either
        "delete_<file/folder_name>" or "keep_<file_name>" '''

import os
import argparse
import sys

relevantFolders = ["Desktop","Downloads", ".Trash"]
allFiles = []
allFolders = []
args = getArgs()

def main():
    method = args.method
    if method == "mark" or method is None:
        if args.path is None and 'root' not in kwargs:
            markForRemoval()
        else:
            if 'root' in kwargs:
                markForRemoval(root=kwargs['root'])
            elif args.path is not None:
                markForRemoval(root=args.path)

        if(args.verbose):
            printItems(allFiles,"Files")
            printItems(allFolders,"Folders")
            totalItems = len(allFiles)+len(allFolders)
            print("You are about to get rid of {} items. {} folders and {} files.".format(totalItems, len(allFiles),len(allFolders)))

    elif method == "unmark":
        if args.path is None and 'root' not in kwargs:
            unmark()
        else:
            if 'root' in kwargs:
                unmark(root=kwargs['root'])
            elif args.path is not None:
                unmark(root=args.path)


def markForRemoval(**path):
    toplevelDirectory = os.getcwd()

    if ('root' in path):
        currentDir = path['root']
        walkTree(currentDir)
    else:
        for folder in relevantFolders:
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
        os.chdir(dpath)
        print(dpath+": ")
        for directory in dirs:
            if ( (directory not in relevantFolders) and (not directory.startswith("keep_")) ):
                if not directory.startswith("delete_"):
                    tempName = prefix+directory
                    try:
                        os.rename(directory,tempName)
                        if(args.verbose):
                            print(directory,"-->",tempName)
                        allFolders.append(directory)
                    except OSError as e:
                        print("ERROR: {} - {}".format(e.filename,e.strerror))
                elif directory.startswith("delete_"):
                    allFolders.append(directory)
        for filename in files:
            if filename != script and not filename.startswith("keep_"):
                if not filename.startswith("delete_") :
                    tempName = prefix+filename
                    try:
                        os.rename(filename,tempName)
                        if(args.verbose):
                            print(filename,"-->",tempName)
                        allFiles.append(filename)
                    except OSError as e:
                        print("ERROR: {} - {}".format(e.filename,e.strerror))
                elif filename.startswith("delete_"):
                    allFiles.append(filename)
        print("")

def printItems(items, typeOfItem):
    print(typeOfItem+" to be deleted: ")
    for item in items:
        print(item, end=",\n")

def unmark(**path):
    if 'root' in path:
        currentDir = path['root']
    else:
        currentDir = os.getcwd()

    print(currentDir)

    for dpath, dirs, files in os.walk(currentDir, topdown=False):
        os.chdir(dpath)
        for directory in dirs:
            if directory.startswith("delete_"):
                try:
                    os.rename(directory, directory[7:])
                    if(args.verbose):
                        print(directory,"-->",directory[7:])
                except OSError as e:
                    print("ERROR: {} - {}".format(e.filename,e.strerror))
        for filename in files:
            if filename.startswith("delete_"):
                try
                    os.rename(filename,filename[7:])
                    if (args.verbose):
                        print(filename,"-->",filename[7:])
                except OSError as e:
                    print("ERROR: {} - {}".format(e.filename,e.strerror))

def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-m", "--method", help="the name of the task to perform: 'mark' to label the items to be deleted or remove the \
        label that was set previously", choices=["mark","unmark"])
    parse.add_argument("-p","--path",help="The path to the root directory of the tree to rename the files and folders from")
    parse.add_argument("-v","--verbose", help="Forces the script to print its current activity",action="store_true")
    args = parse.parse_args()
    return args

if __name__ == "__main__":
    print("running as main program")
    main()
