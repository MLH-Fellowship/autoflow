import os
import click
import subprocess
from autoflow.scripts.shell import proc, runCommand

def create(projectDir,dependencies):
    os.mkdir(projectDir)
    os.chdir(projectDir)
    subprocess.run(['python','-m','venv','env'])
    runCommand(bytes(f'. {projectDir}/env/bin/activate\n','utf-8'))
    if dependencies is not None:
        click.echo('🔥 Installing dependencies')
        runCommand(bytes(f'pip install {dependencies}\n','utf-8'))
        proc.communicate()
    with open('app.py',"w") as file:
        file.close()