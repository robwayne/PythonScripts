#!/usr/bin/env python3

''' A script to work in tandem with purge.py. Renames all the files in certain directories to either
        "delete_<file/folder_name>" or "keep_<file_name>" '''

import os
import argparse
import sys



def rename():
    newFolderName = ""
    prefix = "delete_"
    currentDir = os.getcwd()
    protectedFolders = ["Desktop","Downloads", "PopcornTime", ".Trash"]
    for dpath, dirs, files in os.walk(currentDir, topdown=False):
        os.chdir(dpath)
        for directory in dirs:
            if ( (directory is not in protectedFolders) and (not directory.startswith("keep_")) ):
                if not directory.startswith("delete_"):
                    newFolderName = prefix+directory
                    os.rename(directory,newFolderName)



# def getArgs():
#     parse = argparse.ArgumentParser()
#
#     parse.add_argument("-t","--renametype", help="the type of renaming that should happen to the files. Sets to delete by default.", choices=["delete", "keep"])
#     parse.add_argument("-e","--extension", help="extension of file to rename. Required if 'keep' is specified to renametype.")
#     parse.add_argument("-p","--path", help="root path of the directories to rename")
#     args = parse.parse_args()
#
#     if(args.keep == "keep"):
#         assert args.extension is not None and args.path is not None, "{} requires an --extension and --path argument to be \
#         specified if 'keep' is set as --renametype ".format(sys.argv[0])
#
#     return args
