#!/usr/bin/env python3.5



import os
import argparse
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#inspiration from https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory

class Watcher:
    def __init__(self, **kwargs):
        self.observer = Observer()
        if ('path' in kwargs):
            self.path = os.path.abspath(kwargs['path'])
        else:
            self.path = os.path.abspath(".")

        if 'recursive' in kwargs:
            self.recursive = kwargs[recursive]
        else:
            self.recursive = False


    def run(self):
        eventHandler = Handler()
        print(self.path)
        self.observer.schedule(eventHandler,self.path,recursive=self.recursive)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Error")
        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_created(self,event):
        if(event.is_directory):
            print("Folder: ",event.src_path, "was created.")
        else: print("File: ",event.src_path, "was created.")
    def on_modified(self,event):
        if(event.is_directory):
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
    watcher.run()

if __name__ == "__main__":
    main()
