#!/usr/bin/env 3.5

#inspiration from https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory

import os
import argparse
from watchdog.observers import Observe
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, **kwargs):
        self.observer = Observe()
        if ('path' in kwargs):
            self.path = os.path.abspath(kwargs['path'])
        else:
            self.path = obs.path.abspath('.')

        if 'recursive' in kwargs:
            self.recursive = kwargs[recursive]
        else:
            self.recursive = False


    def run(self):
        eventHandler = Handler()
        self.observer.schedule(eventHandler,self.path,recursive=self.recursive)
        self.observer.start()
        try:
            while True:
                sleep(5)
        except:
            self.observer.stop()
            print("Error")
        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_created(event):
        if(event.is_dir):
            print("Folder: ",event.src_path, "was created.")
        else: print("File: ",event.src_path, "was created.")
    def on_modified(event):
        if(event.is_dir):
            print("Folder: ",event.src_path, "was modified.")
        else: print("File: ",event.src_path, "was modified.")


def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-p", "--path", help="The absolute path to the the directory to observe")
    parse.add_argument("-r", "--recursive", help="Observe / Watch the directory recursively to include subdirectories")
    args = parse.parse_args()
    return args

def main():
    args = getArgs()
    if args.path and args.recursive:
        watcher = Watcher(path=args.path,recursive=args.recursive)
    elif args.path and not args.recursive:
        watcher = Watcher(path=args.path)
    elif not args.path and args.recursive:
        watcher = Watcher(recursive=args.recursive)
    else:
        watcher = Watcher()

      
