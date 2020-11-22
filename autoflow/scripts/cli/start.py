import os
import json
import click
import subprocess

from click.decorators import command
from autoflow.env import projectsDir, slash
from autoflow.scripts.shell import runCommand, proc

@click.command()
@click.argument('dir',type=click.STRING)
def start(dir):
        project = projectsDir + slash + dir
    # try:
        os.chdir(project)
        #checks if af-config exists
        isFile = os.path.isfile('af-config.json')
        #creates and adds default data if doesn't
        if isFile:
            with open('af-config.json') as file:
                data = json.load(file)
                file.close()
                runCommand(f'cd {project}\n')
                runCommand('code .\n')
                if 'command' in data.keys():
                    command = data['command']
                    if 'python' in data['type']:
                        runCommand('. ./env/bin/activate\n')
                        runCommand(f'{command}\n')
                        for line in iter(proc.stdout.readline, ''):
                            print(line)
                    elif 'react' in data['type']:
                        runCommand('code .\n')
                        runCommand(f'{command}\n')
                        for line in iter(proc.stdout.readline, ''):
                            print(line)
        subprocess.run([f'gnome-terminal --tab'],shell=True)
    # except:
        # click.echo('😅 Project doesn\'t exists')