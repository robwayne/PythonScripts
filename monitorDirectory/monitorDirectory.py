#!/usr/bin/env python3.5

import os
import argparse
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread

#inspiration from https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory

class Watcher:
    def __init__(self, path, **kwargs):
        self.observer = Observer()
        self.path = path
        if 'recursive' in kwargs:
            self.recursive = kwargs['recursive']
        else:
            self.recursive = False

    def run(self):
        eventHandler = Handler()
        self.observer.schedule(eventHandler,self.path,recursive=self.recursive)
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


def getRealPath(path):
    if path.startswith('~'):
        newPath = os.path.realpath(os.path.expanduser(path))
    elif path.startswith('.'):
        newPath = os.path.abspath(os.path.realpath(path))
    else: newPath = os.path.realpath(path)

    assert os.path.exists(newPath), "Path '{}' is invalid.".format(path)
    return newPath

def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("-p", "--paths", help="The absolute path(s) to the the directory(ies) to be observed.", nargs='+', required=True)
    parse.add_argument("-r", "--recursive", help="Observe / Watch the directory recursively to include subdirectories.", action="store_true")
    args = parse.parse_args()
    args.paths = list(map(getRealPath, args.paths))
    return args

def monitor():
    args = getArgs()
    watchers = []
    if args.paths:
        for path in args.paths:
            if args.recursive:
                watchers.append(Watcher(path=path,recursive=True))
            else:
                watchers.append(Watcher(path=path))
        for watcher in watchers:
            thread = Thread(target=watcher.run)
            thread.start()
            thread.join()

    else:
        print("ERROR: This should NEVER happen: monitoryDirectory.monitor()")
        exit(-1)

if __name__ == "__main__":
    monitor()
