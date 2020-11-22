import click
from autoflow.scripts.cli import jump, new, start

# the main entry point for entry command
@click.group()
def main():
    pass


# adds command for the cli
main.add_command(new.new)
main.add_command(jump.jump)
main.add_command(start.start)

#calls main function once the script runs
if __name__ == '__main__':
    main()
