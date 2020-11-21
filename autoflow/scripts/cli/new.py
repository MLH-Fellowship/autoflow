import os
import subprocess
import click
from autoflow.scripts.shell import shell
from autoflow.env import projectsDir, slash
from autoflow.scripts.create import python, react

#command to create new projects
@click.command()
@click.option('--language','-l',type=click.STRING,required=True)
@click.option('--name','-n',type=click.STRING,required=True)
@click.option('--dependencies','-d',type=click.STRING)
def new(language,name,dependencies):
    try:
        projectDir = projectsDir + slash + name
        if not os.path.isdir(projectDir):
            click.echo('🔥 Creating your awesome project')
            
            if 'python' in language:
                python.create(projectDir,dependencies)
            elif 'react' in language:
                react.create(name,projectDir)
            click.echo('🔥 Project created')
            subprocess.run(['gnome-terminal --tab'],shell=True)
        else:
            click.echo('👉👈Project already exists')
    except:
        click.echo('😅 Couldn\'t create new project')