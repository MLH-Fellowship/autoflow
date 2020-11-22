import os
import subprocess

shell = os.environ.get('SHELL', '/bin/sh')
proc = subprocess.Popen(shell, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True,universal_newlines=True)

def runCommand(command):
    proc.stdin.write(command)
    proc.stdin.flush()