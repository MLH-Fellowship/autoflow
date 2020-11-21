import os
import subprocess

shell = os.environ.get('SHELL', '/bin/sh')
proc = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE ,shell=True)

def runCommand(command):
    proc.stdin.write(command)
    proc.stdin.flush()