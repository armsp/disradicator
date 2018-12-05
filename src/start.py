#!/usr/bin/env python3
import subprocess
import sys

subprocess.Popen(["python3", "appindicator.py"], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.exit(0)