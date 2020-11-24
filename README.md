<p align="center">
 <h1 align="center">🔥 Autoflow 🔥</h1>
 <h3 align="center">Automating your project workflows and making your life easier!</h3>
</p>
<p align="center">
 <img src="https://img.shields.io/github/issues-closed/MLH-Fellowship/autoflow?color=blue&style=for-the-badge" align="center"/>
 <img src="https://img.shields.io/github/issues-pr-closed/MLH-Fellowship/autoflow?color=yellow&style=for-the-badge" align="center"/>
</p>
<hr>

## Introduction 
Welcome to 🔥 Autoflow 🔥, the command-line tool that automates all of your project initializations and project setups!

Using this CLI, you will be able to use your time more productively by working through your project instead of going through tedious parts of the initialization workflow. You'll be able to jump to multiple projects from anywhere, start your project backends more easily, and set up new projects with less commands. 

## Support
 - Languages/Project types supported: <img src="https://img.shields.io/badge/python-%232671E5.svg?&style=for-the-badge&logo=python&logoColor=white&color=darkblue"/> <img src="https://img.shields.io/badge/react%20-%2320232a.svg?&style=for-the-badge&logo=react&logoColor=%2361DAFB"/> <img src="https://img.shields.io/badge/node.js%20-%2343853D.svg?&style=for-the-badge&logo=node.js&logoColor=white"/>
 - OS support: <img src="https://img.shields.io/badge/linux-%232671E5.svg?&style=for-the-badge&logo=linux&logoColor=white&color=purple"/> <img src="https://img.shields.io/badge/macOS-%232671E5.svg?&style=for-the-badge&logoColor=white&color=purple"/>
 - Python versions supported: <img src="https://img.shields.io/pypi/pyversions/django?style=for-the-badge"/>
   
## Get Started

### 1. First, let's clone the repository:
```
git clone https://github.com/MLH-Fellowship/autoflow.git
```

### 2. Next, let's make sure we have a virtual environment set up. 

If you're on Mac OS or Linux, either use:
```
sudo easy_install virtualenv
```
or
```
pip install virtualenv --user
```

If you're on Ubuntu, try:
```
sudo apt-get install python-virtualenv
```

### 3. Then we can move into our autoflow folder and start our virtualenv:
```
cd autoflow
virtualenv venv
. venv/bin/activate
```

### 4. We have successfully activated our virtual environment! Next, let's install our requirements and the package:
```
pip install -r requirements.txt
pip install --editable .
```

### 5. There's one last configuration that needs to be done. First, mv to the package directory:
```
cd ~/.autoflow
```
There, you will find an af-config.json file. This is your global configuration file that enables Autoflow to link to your projects directory, open your text editor,
or push to your GitHub. The defaults are set as below: 
```
{
      "defaultDirectory": Path.home()
      "defaultTextEditor": "nano",
      "github_token": "${{ secrets.GITHUB_TOKEN }}"
}
```
Replace the default directory config with the path to wherever you keep your projects and the default text editor config with whatever you like to use for your editor(ie. "code" for VSCode). The github token config is set up for use in our CI/CD workflow and will not actually work for you. Replace it with your personal access token, which you can generate by going to github.com, going to Settings, clicking on "Developer Settings" on the right-side menu, clicking on "Personal Access Tokens" in the new menu, and clicking "Generate new token" in the right upper corner. 

You are now set up to use Autoflow!

## Usage
In order use Autoflow with any specific project, you will have to have a local configuration file within that project folder called af-config.json. This is how it should be set up:
```
{
     "type": "<project type>",
     "command": "<start server command for project>"
}
```
This is to ensure that the `af start` command works properly and starts your project backend if you have one. The project types supported are listed in the [Support](#support) section.

In order to have these instructions again and see the commands you can run, run this command in your terminal: `af --help`.
This will give you everything you need to start using this package and is similar to the instructions found here. 

## An Example

<img src="https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/jump.gif" alt="autoflow jump"/>
<img src="https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/new.gif" alt="autoflow new"/>
<img src="https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/start.gif" alt="autoflow start"/>
<img src="https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/gli-cli.gif" alt="autoflow git-cli"/>

## Tech Stack:
 - **CLI Backend**: <img src="https://img.shields.io/badge/click%20-%232671E5.svg?&style=for-the-badge&logo=data:image/png;base64,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&logoColor=white&color=purple"/>
 - **Languages**: <img src="https://img.shields.io/badge/python-%232671E5.svg?&style=for-the-badge&logo=python&logoColor=white&color=darkblue"/> <img src="https://img.shields.io/badge/bash-%232671E5.svg?&style=for-the-badge&logo=gnu%20bash&logoColor=white&color=darkgreen"/>
 - **Testing**: <img src="https://img.shields.io/badge/pytest-%232671E5.svg?&style=for-the-badge&logo=python&logoColor=white&color=darkred"/> <img src="https://img.shields.io/badge/click.testing%20-%232671E5.svg?&style=for-the-badge&logo=data:image/png;base64,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&logoColor=white&color=darkorange"/>
 - **CI/CD**: <img src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white&color=blue"/>
 - **Version Control**: <img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white&color=green"/> <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

## Testing
We used multiple tools to enable unit testing and CI/CD for this project. For testing, we used pytest and click.testing to invoke the commands and test their outputs in several situations in one test script. This test script is setup to work with GitHub Actions, which is what we used for our CI/CD workflow. We were able to implement unit tests in this way, and all the tests are commented through to enable easy read-through for other potential contributors. 

GitHub actions allowed us to run multiple builds with multiple operating systems(macOS and Ubuntu) and multiple python versions(3.6, 3.7, 3.8). Once we add support for Windows, we will add that build to our matrix as well. As of right now, every time we push to the main branch of this project or merge something to the main branch, the GitHub actions testing workflow will run. 

We will also be using releases to keep track of our versions. Our version released on November 24th will be version 1. 

## Contributing
Autoflow is fully Open-Source and open for contributions! We request you to respect our contribution guidelines as defined in our [CODE OF CONDUCT](https://github.com/MLH-Fellowship/autoflow/blob/main/CODE_OF_CONDUCT.md) and [CONTRIBUTING GUIDELINES](https://github.com/MLH-Fellowship/autoflow/blob/main/CONTRIBUTING.md).

## Contributors
 - [Dipanwita Guhathakurta](https://github.com/susiejojo)
 - [Saurabh Kumar Suryan](https://github.com/sksuryan)
 - [Shilpita Biswas](https://github.com/sh-biswas)

Made with ❤️️ by Team Autoflow as part of MLH Explorer Fall Fellowship 2020 Sprint 4.
