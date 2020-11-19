import click
from autoflow.scripts.new import new

# the main entry point for entry command
@click.group()
def main():
    pass

# a random command
@click.command()
def hello():
    click.echo('Hello')


# adds command for the cli
main.add_command(hello)
main.add_command(new)

#calls main function once the script runs
if __name__ == '__main__':
    main()
