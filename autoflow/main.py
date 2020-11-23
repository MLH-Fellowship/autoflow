import click, os, git
from autoflow.scripts.cli import jump, new, start
# from autoflow.scripts.new import new
from autoflow.scripts.git_connect import git_connect
from autoflow.env import github_token,readmePath
# the main entry point for entry command
@click.group()
def main():
    """
    Welcome to Autoflow, the command-line tool that automates all of your project
    initializations and project setups!

    We currently support macOS and Windows. The project types we support are Python, Node,
    and React. 
    """
    pass

# a random command
@click.command()
def hello():
    """
    Test click
    """
    click.echo('Hello')

# commands for github
@click.command()
def git_cli():
    """
    Initializes a git repository in your desired directory
    """
    # click.echo("git")
    click.echo('Taking your Access token from the current env...')
    git_obj = git_connect(github_token)
    gitDir = os.getcwd()+"/.git"
    print (gitDir)
    repo_path = ""
    remote_flag = 1
    if os.path.isdir(gitDir):
        click.echo("Git is initialised locally already.")
        repo = git.Repo(".", search_parent_directories=True) 
        try:
            repo_path = repo.remote("origin").url
            click.echo("Using existing remotes...")
            remote_flag = 0
        except:
            click.echo("You have a local git repository but no remote.")
    if (remote_flag==1):
        if (click.confirm("Do you want to create a new repo?")):
            repo_name = click.prompt("Enter repo name",type=str)
            git_obj.create_repo(repo_name)
        else:
            if (click.confirm("Do you want to link to an existing repository?")):
                repo_name = click.prompt("Enter repo name",type=str)
            git_obj.existing_repo(repo_name)
        os.system("git init")
        repo_path = git_obj.repo.html_url
        os.system("git remote add origin "+str(repo_path))
        
    print ("repo_path: ",repo_path)
    
    click.echo("Linked to : "+str(repo_path))
    
    cur_proj = os.getcwd()
    print ("cur_dir: ",cur_proj)

    readme = open(readmePath,"r")
    readmetext = readme.read()
    readme.close()

    readmefile = open("README.md","w")
    readmefile.write(readmetext)
    readmefile.close()

    gitignorefile = open(".gitignore","w")
    gitignorefile.write("env/")
    gitignorefile.close()

    os.system("git add .")
    os.system("git commit -m \"Add initial project\"")
    os.system("git push origin master")
    click.echo("Project started in master branch of "+repo_path)
    if (click.confirm("Let us add your teammates as collaborators!")):
        colab_name = click.prompt("Enter the Github handle of collaborator you want to add",type=str)
        git_obj.add_colabs(colab_name)     


# adds command for the cli
main.add_command(new.new)
main.add_command(jump.jump)
main.add_command(start.start)
main.add_command(git_cli)

#calls main function once the script runs
if __name__ == '__main__':
    main()
