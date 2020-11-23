from pathlib import Path

#defines home as default directory for projects
defaultDirectory = str(Path.home())
#defines nano as default editor for projects
defaultTextEditor = 'nano'
#defines a secret token from Github for github token
github_token = '${{secrets.GITHUB_TOKEN}}'