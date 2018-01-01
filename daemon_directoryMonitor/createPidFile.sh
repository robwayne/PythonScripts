#!/bin/bash

daemon="daemon_directoryMonitor.py"
pidfile=daemon_pid.pid

python $daemon start &
PID=$!
echo $PID > $pidfile
