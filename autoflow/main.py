import click, os, git
from autoflow.scripts.cli import jump, new, start
# from autoflow.scripts.new import new
from autoflow.scripts.git_connect import git_connect
from autoflow.env import github_token,readmePath
# the main entry point for entry command
@click.group()
def main():
    """
    Welcome to 🔥 Autoflow 🔥, the command-line tool that automates all of your project
    initializations and project setups!

    We currently support macOS and Linux. The project types we support are Python, Node,
    and React. The Python versions we support are 3.6, 3.7, and 3.8.

    Once you install Autoflow on your machine, be sure to configure your global Autoflow
    configuration file with the path to your default project directory, the text editor you
    normally use, and your Github personal access token that you can generate at www.github.com.
    
    You can access the global configuration file by installing this package and changing your
    current working directory to .autoflow by using 'cd ~/.autoflow' There is a default af-config.json
    already there with these configurations:

    \b
        {
            "defaultDirectory": Path.home()
            "defaultTextEditor": "nano",
            "github_token": "${{ secrets.GITHUB_TOKEN }}"
        }

    The configuration for the github token is just for testing purposes. You will need to replace that configuration with
    your own access token. 

    Be sure to also configure a local configuration file for each project you have by opening an af-config.json
    in your project folder. Have this data filled in in your file:

    \b
        {
            "type": "<project type>",
            "command": "<start server command for project>"
        }

    When you use our 'af start' command for your project, it will read off this file 
    to start the backend for your project and directly open your project. 

    Have a great time hacking!
    """
    pass

# a random command
@click.command(name='hello')
def hello():
    """
    Test click
    """
    click.echo('Hello')

# commands for github
@click.command(name='git-cli')
def git_cli():
    """
    Initializes a git repository in your desired directory

    Must be in the desired directory to use this command
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
