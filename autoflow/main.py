import click
import os
from autoflow.scripts.new import new
from autoflow.scripts.git_connect import git_connect

# the main entry point for entry command
@click.group()
def main():
    pass

# a random command
@click.command()
def hello():
    click.echo('Hello')

# commands for github
@click.command()
@click.argument('acc_token', envvar='GITHUB_TOKEN')
def git(acc_token):
    # click.echo("git")
    click.echo('Taking your Access token from the current env...')
    git_obj = git_connect(acc_token)
    if (click.confirm("Do you want to create a new repo?")):
        repo_name = click.prompt("Enter repo name",type=str)
        git_obj.create_repo(repo_name)
        click.echo("Repository created at: "+git_obj.repo.html_url)
    else:
        if (click.confirm("Do you want to link to an existing repository?")):
            repo_name = click.prompt("Enter repo name",type=str)
            git_obj.existing_repo(repo_name)
            click.echo("Linked to: "+git_obj.repo.html_url)
        else:
            click.echo("You have chosen not to link your project to Github. For version control I'll set up a local git project")
    os.system("git init")
    repo_link = git_obj.repo.clone_url
    os.system("git remote add origin "+repo_link)
    readme_file = open("../best_readme_template.md","r")
    readmetext = readme_file.read()
    git_obj.add_template_readme(readmetext)
    if (click.confirm("Let us add your teammates as collaborators!")):
        colab_name = click.prompt("Enter the Github handle of collaborator you want to add",type=str)
        git_obj.add_colabs(colab_name)

# adds command for the cli
main.add_command(hello)
main.add_command(new)
main.add_command(git)

#calls main function once the script runs
if __name__ == '__main__':
    main()
