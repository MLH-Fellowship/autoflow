import os
import click
import subprocess
from autoflow.scripts.shell import shell
from autoflow.env import projectsDir, slash
from autoflow.scripts.create import python, react, node

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
                react.create(name,projectsDir,dependencies)
            elif 'node' in language:
                node.create(projectDir,dependencies)
            else:
                click.echo('🤦 language not supported')
                return
            click.echo('🔥 Project created')
            subprocess.run(['gnome-terminal --tab'],shell=True)
        else:
            click.echo('👉👈Project already exists')
    except:
        click.echo('😅 Couldn\'t create new project')