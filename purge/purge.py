#!/usr/bin/env python3.5

import os
import argparse
import subprocess
import sys

def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-p","--path",help="The path to the root directory of the tree to rename the files and folders from")
    parse.add_argument("-v","--verbose", help="Forces the script to print its current activity",action="count", default=0)
    args = parse.parse_args()
    return args

relevantFolders = ["Desktop","Downloads", ".Trash"]
args = getArgs()
successfulRemovals = {}
failedRemovals = {}

def main():
    pathProvided = False

    if args.path:
        pathProvided = True
        if(args.verbose >= 2):
            subprocess.call(["markForRemoval.py", "-v", "-p", args.path])
        else:
            subprocess.call(["markForRemoval.py", "-p", args.path])
    elif args.path is None:
        if(args.verbose >= 2):
            subprocess.call(["markForRemoval.py", "-v"])
        else:
            subprocess.call(["markForRemoval.py"])

    if args.verbose >= 2:
        resume = input("Do you want to continue with purge and remove these items? ('yes' , 'no'): ").lower()

        if resume[0] == 'y':
            print("Items will be removed.")
            if pathProvided:
                remove(root=args.path)
            else:
                remove()
        else:
            print("Removal cancelled. Execution of purge stopped.")
    else:
        if pathProvided:
            remove(root=args.path)
        else:
            remove()



def remove(**path):
    topLevelDir = os.getcwd()

    if 'root' in path:
        currentDir = path['root']
        walkTree(currentDir)
    else:
        for folder in relevantFolders:
            currentDir = os.path.join(topLevelDir,folder)
            os.chdir(currentDir)
            walkTree(currentDir)


def walkTree(directoryPath):

    script = sys.argv[0]
    if script.startswith("./"):
        script = script[2:]

    for dpath, dirs, files in os.walk(directoryPath,topdown=False):
        os.chdir(dpath)
        for filename in files:
            if filename.startswith("delete_") and filename != script:
                if args.verbose >= 1:
                    print("removing: ",filename)
                try:
                    os.remove(filename)
                    successfulRemovals[filename] = dpath
                except OSError as e:
                    failedRemovals[(filename,e.strerror)] = dpath
                    print("ERROR: {} - {}".format(e.filename,e.strerror))

        for directory in dirs:
            if directory not in relevantFolders and directory.startswith("delete_"):
                if args.verbose >= 1:
                    print("removing: ",directory)
                    if(os.path.islink(directory)):
                        try:
                            os.unlink(directory)
                            successfulRemovals[directory] = dpath
                        except OSError as e:
                            failedRemovals[(directory,e.strerror)] = dpath
                            print("ERROR: {} - {}".format(e.filename,e.strerror))
                    else:
                        try:
                            os.rmdir(directory)
                            successfulRemovals[directory] = dpath
                        except OSError as e:
                            failedRemovals[(directory,e.strerror)] = dpath
                            print("ERROR: {} - {}".format(e.filename,e.strerror))

    if args.verbose >= 1:
        totalItems = len(successfulRemovals)+len(failedRemovals)
        print("\n{} out of {} item(s) was(were) successfully removed.".format(len(successfulRemovals), totalItems))
        if (len(successfulRemovals)>0):
            print("\nSuccessfully removed:")
            for key in successfulRemovals:
                print(" ",key,"in folder: ",successfulRemovals[key])
        print("\n{} out of {} items failed during removal.".format(len(failedRemovals), totalItems))
        if(len(failedRemovals)>0):
            print("\nFailed while removing:")
            for key in failedRemovals:
                key1, key2 = key
                print(" ",key1,"in folder: ",failedRemovals[key], " - ",key2)



def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-p","--path",help="The path to the root directory of the tree to rename the files and folders from")
    parse.add_argument("-v","--verbose", help="Forces the script to print its current activity",action="count", default=0)
    args = parse.parse_args()
    return args


if __name__ == "__main__":
    main()
