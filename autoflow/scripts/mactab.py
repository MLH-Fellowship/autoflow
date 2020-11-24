from subprocess import Popen, PIPE
import sys
import os

def osascript(scpt):
     p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
     stdout, stderr = p.communicate(scpt.encode('utf-8'))
     return stdout, stderr

def openTab():
    script = f"""
            tell application "System Events"
                tell process "Terminal" to keystroke "t" using command down
            end
            tell application "Terminal"
                activate
                do script with command "cd {os.getcwd()}" in window 1
            end tell
            """
    stdout, stderr = osascript(script)
    if stderr:
        sys.stderr.write('Error in Applescript: {}\n'.format(stderr))