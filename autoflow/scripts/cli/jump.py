import os
import click
import subprocess
from sys import platform
from autoflow.scripts.mactab import openTab
from autoflow.env import projectsDir, slash

@click.command()
@click.argument('dir',type=click.STRING)
def jump(dir):
    """
    Jumps to your specified project directory
    """
    project = projectsDir + slash + dir
    try:
        os.chdir(project)
        if platform == "linux" or platform == "linux2":
            subprocess.run([f'gnome-terminal --tab'],shell=True)
        elif platform == "darwin":
            openTab()

    except:
        click.echo('😅 Project doesn\'t exists')