#!/usr/bin/env python3.5

import argparse
import os
import time
from daemon import Daemon
from directoryMonitor import Watcher


class MonitorDaemon(Daemon):
    def run(self):
        watcher = Watcher()
        watcher.run()

def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument("operation", help="Operation to follow", choices=["start", "restart", "stop"])
    args = parse.parse_args()
    return args


def main():
    args = getArgs()
    pidfile = os.path.join(os.getcwd(),'daemon_pid.pid')
    daemon = MonitorDaemon(pidfile)
    if args.operation == "start":
        daemon.start()
    elif args.operation == "restart":
        daemon.restart()
    elif args.operation == "stop":
        daemon.stop()



if __name__ == "__main__":
    main()
