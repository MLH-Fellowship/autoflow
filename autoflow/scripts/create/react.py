import os
import click
from autoflow.scripts.shell import proc, runCommand

def create(name,projectDir):
    click.echo('⏳ Create React App takes some time')
    click.echo('☕ Grab some coffee')
    runCommand(bytes(f'npx create-react-app {name}\n','utf-8'))
    proc.communicate()
    os.chdir(projectDir)