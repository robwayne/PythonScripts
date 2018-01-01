#!/usr/bin/env python3.5

import os
import argparse
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#inspiration from https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory

class Watcher:
    def __init__(self, **kwargs):
        self.observer = Observer()
        if ('paths' in kwargs):
            self.paths = list(map(self.getRealPath,kwargs['paths']))
        else:
            self.paths = [os.getcwd()]

        if 'recursive' in kwargs:
            self.recursive = kwargs['recursive']
        else:
            self.recursive = False

    def getRealPath(self, path):
        if path.startswith('~'):
            newPath = os.path.realpath(os.path.expanduser(path))
        elif path.startswith('.'):
            newPath = os.path.abspath(os.path.realpath(path))
        else: newPath = os.path.realpath(path)

        assert os.path.exists(newPath), "Path '{}' is invalid.".format(path)
        return newPath



    def begin(self):
        for path in self.paths:
            pid = os.fork()
            if pid >= 0:
                self.run(path)
                

    def run(self, path):
        eventHandler = Handler()
        print(self.paths)
        self.observer.schedule(eventHandler,path,recursive=self.recursive)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_created(self,event):
        path = os.path.dirname(event.src_path)
        subprocess.call(["markForRemoval.py", "-p", path])

def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-p", "--paths", help="The absolute path(s) to the the directory(ies) to be observed.", nargs='+')
    parse.add_argument("-r", "--recursive", help="Observe / Watch the directory recursively to include subdirectories.", action="store_true")
    args = parse.parse_args()
    return args

def monitor():
    args = getArgs()
    if args.paths and args.recursive:
        watcher = Watcher(paths=args.paths,recursive=args.recursive)
    elif args.paths and not args.recursive:
        watcher = Watcher(paths=args.paths)
    elif not args.paths and args.recursive:
        watcher = Watcher(recursive=args.recursive)
    else:
        watcher = Watcher()
    watcher.begin()

if __name__ == "__main__":
    monitor()
