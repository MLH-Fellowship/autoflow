import os
import json
from pathlib import Path

#selects slash type depending on OS
slash = ''
if os.name == 'posix':
    slash = '/'
else:
    slash = '\\'

#defines name of the global config folder
configFolderName = '.autoflow'
#defines name of the config file
configFileName = 'af-config.json'

#path for home directory
home = str(Path.home())
#path for .autoflow folder
configFolder = home + slash + configFolderName
#filepath for af-config
configFilePath = configFolder + slash + configFileName

#contains the default directory of projects
projectsDir = ''
#opens af-config file to get global data
with open(configFilePath) as file:
    data = json.load(file)
    projectsDir = data['defaultDirectory']
    os.chdir(projectsDir)
    file.close()