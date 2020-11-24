from pathlib import Path

# defines home as default directory for projects
if str(Path.home()) == '/home/runner':
    defaultDirectory = '/home/runner/work/autoflow/autoflow'
elif str(Path.home()) == '/Users/runner':
    defaultDirectory == '/Users/runner/work/autoflow/autoflow'
else:
    defaultDirectory = str(Path.home())
# defines nano as default editor for projects
defaultTextEditor = 'nano'
# defines a secret token from Github for github token
github_token = '${{secrets.GITHUB_TOKEN}}'