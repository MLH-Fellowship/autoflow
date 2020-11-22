import os
import click
import subprocess
from autoflow.env import projectsDir, slash

@click.command()
@click.argument('dir',type=click.STRING)
def jump(dir):
    project = projectsDir + slash + dir
    try:
        os.chdir(project)
        subprocess.run([f'gnome-terminal --tab'],shell=True)
    except:
        click.echo('😅 Project doesn\'t exists')