import os
import click
from autoflow.scripts.shell import proc, runCommand

def create(name,projectDir):
    click.echo('⏳ Create React App takes some time')
    click.echo('☕ Grab some coffee')
    runCommand(f'npx create-react-app {name}\n')
    proc.communicate()
    os.chdir(projectDir)