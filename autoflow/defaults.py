from pathlib import Path
import os

# defines home as default directory for projects
if 'GITHUB_WORKSPACE' in os.environ:
    defaultDirectory = '${{GITHUB_WORKSPACE}}'
else:
    defaultDirectory = str(Path.home())
# defines nano as default editor for projects
defaultTextEditor = 'nano'
# defines a secret token from Github for github token
github_token = '${{secrets.GITHUB_TOKEN}}'