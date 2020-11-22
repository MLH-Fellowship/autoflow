import os
import json
import click
from autoflow.scripts.cli import jump, new, start
from autoflow.defaults import defaultDirectory, defaultTextEditor
from autoflow.env import configFilePath, configFolder, configFolderName

#creates a dict for default data
defaultData = {
    'defaultDirectory': defaultDirectory,
    'defaultTextEditor': defaultTextEditor
}

# the main entry point for entry command
@click.group()
def main():
    #checks if autoflow config folder exists
    isDir = os.path.isdir(configFolder)
    #creates a folder if it doesn't
    if not isDir:
        os.mkdir(configFolderName)
    
    #checks if af-config exists
    isFile = os.path.isfile(configFilePath)
    #creates and adds default data if doesn't
    if not isFile:
        with open(configFilePath,"w") as file:
            data = json.dumps(defaultData,sort_keys=True,indent=4)
            file.write(data)
            file.close()


# adds command for the cli
main.add_command(new.new)
main.add_command(jump.jump)
main.add_command(start.start)

#calls main function once the script runs
if __name__ == '__main__':
    main()
