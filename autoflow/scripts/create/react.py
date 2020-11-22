import os
import click
import subprocess

def create(name,projectsDir,dependencies):
    click.echo('⏳ Create React App takes some time')
    click.echo('☕ Grab some coffee')
    os.chdir(projectsDir)
    subprocess.run([f'npx create-react-app {name}'],shell=True)
    os.chdir(name)
    if dependencies:
        subprocess.run([f'npm install {dependencies}'],shell=True)