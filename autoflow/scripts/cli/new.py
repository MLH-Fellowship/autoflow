import os
import click
import subprocess
from sys import platform
from autoflow.scripts.mactab import openTab
from autoflow.env import projectsDir, slash
from autoflow.scripts.create import python, react, node

#command to create new projects
@click.command()
@click.option('--language','-l',type=click.STRING,required=True, help = 'Desired project type or language(Python, Node, React)')
@click.option('--name','-n',type=click.STRING,required=True, help = 'Desired project name')
@click.option('--dependencies','-d',type=click.STRING, help = 'Desired project dependencies')
def new(language,name,dependencies):
    """
    Starts a new project based on your desired project type
    """
    try:
        projectDir = projectsDir + slash + name
        if not os.path.isdir(projectDir):
            click.echo('🔥 Creating your awesome project')
            
            if 'python' in language:
                python.create(projectDir,dependencies)
            elif 'react' in language:
                react.create(name,projectsDir,dependencies)
            elif 'node' in language:
                node.create(projectDir,dependencies)
            else:
                click.echo('🤦 language not supported')
                return
            click.echo('🔥 Project created')
            if platform == "linux" or platform == "linux2":
                subprocess.run([f'gnome-terminal --tab'],shell=True)
            elif platform == "darwin":
                openTab()
        else:
            click.echo('👉👈Project already exists')
    except:
        click.echo('😅 Couldn\'t create new project')