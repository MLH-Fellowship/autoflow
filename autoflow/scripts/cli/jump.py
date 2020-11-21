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
    except:
        click.echo('😅 Project doesn\'t exists')

    subprocess.run([f'gnome-terminal --tab'],shell=True)







    # exec('../bin/e.sh')
    # subprocess.run([shell],shell=True)
    # subprocess.Popen(['e.sh'])
    # subprocess.run([f'gnome-terminal --tab -- '],shell=True)