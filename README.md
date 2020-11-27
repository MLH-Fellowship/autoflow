<p align="center">
 <h1 align="center">🔥 Autoflow 🔥</h1>
 <h3 align="center">Automating your project workflows and making your life easier!</h3>
</p>
<p align="center">
 <img src="https://img.shields.io/github/issues-closed/MLH-Fellowship/autoflow?color=blue&style=for-the-badge" align="center"/>
 <img src="https://img.shields.io/github/issues-pr-closed/MLH-Fellowship/autoflow?color=yellow&style=for-the-badge" align="center"/>
</p>
<hr>

## 🔥 Introduction 
Welcome to 🔥 Autoflow 🔥, the command-line tool that automates all of your project initializations and project setups!

Using this CLI, you will be able to use your time more productively by working through your project instead of going through tedious parts of the initialization workflow. You'll be able to jump to multiple projects from anywhere, start your project backends more easily, and set up new projects with less commands. 

## 🔥 Support
 - Languages/Project types supported: <img src="https://img.shields.io/badge/python-%232671E5.svg?&style=for-the-badge&logo=python&logoColor=white&color=darkblue"/> <img src="https://img.shields.io/badge/react%20-%2320232a.svg?&style=for-the-badge&logo=react&logoColor=%2361DAFB"/> <img src="https://img.shields.io/badge/node.js%20-%2343853D.svg?&style=for-the-badge&logo=node.js&logoColor=white"/>
 - OS support: <img src="https://img.shields.io/badge/linux-%232671E5.svg?&style=for-the-badge&logo=linux&logoColor=white&color=purple"/> <img src="https://img.shields.io/badge/macOS-%232671E5.svg?&style=for-the-badge&logoColor=white&color=purple"/>
 - Python versions supported: <img src="https://img.shields.io/pypi/pyversions/django?style=for-the-badge"/>
   
## 🔥 Get Started

### Let's install our package!

```pip install python-af```

or

```pip3 install python-af```

### There's also one configuration that needs to be done. First, move to the package directory:

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

## 🔥 Usage
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

## 🔥 Autoflow in Action

#### 🔥 Command: *af jump*

![autoflow git-cli](https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/jump.gif)


#### 🔥 Command: *af new*

![autoflow git-cli](https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/new.gif)

#### 🔥 Command: *af start*

![autoflow git-cli](https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/start.gif)

#### 🔥 Command: *af git-cli*

![autoflow git-cli](https://github.com/MLH-Fellowship/autoflow/blob/main/screenshots/git-cli.gif)

## 🔥 Tech Stack:
 - **CLI Backend**: <img src="https://img.shields.io/badge/click%20-%232671E5.svg?&style=for-the-badge&logoColor=white&color=purple"/>
 - **Languages**: <img src="https://img.shields.io/badge/python-%232671E5.svg?&style=for-the-badge&logo=python&logoColor=white&color=darkblue"/> <img src="https://img.shields.io/badge/bash-%232671E5.svg?&style=for-the-badge&logo=gnu%20bash&logoColor=white&color=darkgreen"/>
 - **Testing**: <img src="https://img.shields.io/badge/pytest-%232671E5.svg?&style=for-the-badge&logo=python&logoColor=white&color=darkred"/> <img src="https://img.shields.io/badge/click.testing%20-%232671E5.svg?&style=for-the-badge&logoColor=white&color=darkorange"/>
 - **CI/CD**: <img src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white&color=blue"/>
 - **Version Control**: <img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white&color=green"/> <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

## 🔥 Testing
We used multiple tools to enable unit testing and CI/CD for this project. For testing, we used pytest and click.testing to invoke the commands and test their outputs in several situations in one test script. This test script is setup to work with GitHub Actions, which is what we used for our CI/CD workflow. We were able to implement unit tests in this way, and all the tests are commented through to enable easy read-through for other potential contributors. 

GitHub actions allowed us to run multiple builds with multiple operating systems(macOS and Ubuntu) and multiple python versions(3.6, 3.7, 3.8). Once we add support for Windows, we will add that build to our matrix as well. As of right now, every time we push to the main branch of this project or merge something to the main branch, the GitHub actions testing workflow will run. 

We will also be using releases to keep track of our versions. Our version released on November 24th will be version 1. 

## 🔥 What We Learned
 - Subprocesses in Python
 - Testing with pytest
 - Linting with flake8
 - Setting up CI/CD with GitHub Actions
 - Building a CLI with Python
 - Publishing a package to PyPi
 - Using the GitHub API for our CLI
 
 In regards to soft skills, we learned to ask for help from our MLH mentors instead of trying to solve problems with little success. 

## 🔥 Contributing
Autoflow is fully Open-Source and open for contributions! We request you to respect our contribution guidelines as defined in our [CODE OF CONDUCT](https://github.com/MLH-Fellowship/autoflow/blob/main/CODE_OF_CONDUCT.md) and [CONTRIBUTING GUIDELINES](https://github.com/MLH-Fellowship/autoflow/blob/main/CONTRIBUTING.md).

## ❤ Contributors
 - [Dipanwita Guhathakurta](https://github.com/susiejojo)
 - [Saurabh Kumar Suryan](https://github.com/sksuryan)
 - [Shilpita Biswas](https://github.com/sh-biswas)

Made with ❤️️ by Team Autoflow as part of MLH Explorer Fall Fellowship 2020 Sprint 4.
