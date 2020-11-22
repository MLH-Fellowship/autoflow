import os
import subprocess

def create(projectDir,dependencies):
    os.mkdir(projectDir)
    os.chdir(projectDir)
    subprocess.run(['npm init'],shell=True)
    if dependencies:
        subprocess.run([f'npm install {dependencies}'],shell=True)