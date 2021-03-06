#!/Users/robudhabi/anaconda/bin/python3.5

import os
import argparse
import subprocess
#Author: Robert Gordon
#Date: Jan 1, 2018

def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-p","--path",help="The path to the root directory of the tree to rename the files and folders from")
    parse.add_argument("-v","--verbose", help="Forces the script to print its current activity",action="count", default=0)
    args = parse.parse_args()
    return args

purgeableFolders = ["Desktop","Downloads", ".Trash"]
args = getArgs()
successfulRemovals = {}
failedRemovals = {}

def main():
    pathProvided = False
    
    if args.verbose >= 2 and args.path:
        pathProvided = True
        subprocess.call(["markForRemoval.py", "-v", "-p", args.path])
    elif args.verbose >= 2 and not args.path:
        subprocess.call(["markForRemoval.py", "-v"])
    elif args.verbose < 2 and args.path:
        subprocess.call(["markForRemoval.py", "-p", args.path])
    else:
        subprocess.call(["markForRemoval.py"])
    
    if args.verbose >= 2:
        resume = input("Do you want to continue with purge and remove these items? ('yes' , 'no'): ").lower()
        
        if resume.startswith('y'):
            print("Items will be removed.")
            if pathProvided:
                remove(root=args.path)
            else:
                remove()
        else:
            if pathProvided:
                subprocess.call(["markForRemoval.py", "-m", "unmark",  "-p", args.path])
            else:
                subprocess.call(["markForRemoval.py", "-m","unmark"])
            print("Removal cancelled. Execution of purge stopped.")
    else:
        if pathProvided:
            remove(root=args.path)
        else:
            remove()



def remove(**path):
    topLevelDir = os.path.dirname(os.path.realpath(__file__))
    
    if 'root' in path:
        currentDir = path['root']
        walkTree(currentDir)
    else:
        for folder in purgeableFolders:
            currentDir = os.path.join(topLevelDir,folder)
            os.chdir(currentDir)
            walkTree(currentDir)

def delete(items):
    for item in items:
        if item.startswith("delete_"):
            if args.verbose >= 1:
                print("removing: ",filename)



def walkTree(directoryPath):
    for dpath, dirs, files in os.walk(directoryPath,topdown=False):
        os.chdir(dpath)
        for filename in files:
            if filename.startswith("delete_"):
                if args.verbose >= 1:
                    print("removing: ",filename)
                try:
                    os.remove(filename)
                    successfulRemovals[filename] = dpath
                except OSError as e:
                    failedRemovals[(filename,e.strerror)] = dpath
                    print("ERROR: {} - {}".format(e.filename,e.strerror))
    
        for directory in dirs:
            if directory not in purgeableFolders and directory.startswith("delete_"):
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
    if args.path:
        args.path = getRealPath(args.path)
    return args

def getRealPath(path):
    if path.startswith('~'):
        newPath = os.path.realpath(os.path.expanduser(path))
    elif path.startswith('.'):
        newPath = os.path.abspath(os.path.realpath(path))
    else: newPath = os.path.realpath(path)

assert os.path.exists(newPath), "Path '{}' is invalid.".format(path)
return newPath


if __name__ == "__main__":
    main()

