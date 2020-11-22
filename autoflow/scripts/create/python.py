import os
import click
import subprocess
from autoflow.scripts.shell import proc, runCommand

def create(projectDir,dependencies):
    os.mkdir(projectDir)
    os.chdir(projectDir)
    subprocess.run(['python3','-m','venv','env'])
    runCommand(f'. {projectDir}/env/bin/activate\n')
    if dependencies is not None:
        click.echo('🔥 Installing dependencies')
        runCommand(f'pip install {dependencies}\n')
        proc.communicate()
    with open('app.py',"w") as file:
        file.close()