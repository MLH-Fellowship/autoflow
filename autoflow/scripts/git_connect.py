from github import Github

class git_connect:
    def __init__(self,acc_token):
        self.g = Github(acc_token)
        self.user = self.g.get_user()
    def create_repo(self,repo_name):
        self.repo = self.user.create_repo(repo_name)
    def existing_repo(self,repo_name):
        repo_path = str(self.user.login)+"/"+repo_name
        self.repo = self.g.get_repo(repo_path)
    def add_colabs(self,colab_name):
        self.repo.add_to_collaborators(colab_name,permission="push")
    def add_template_readme(self,readmetext):
        self.repo.create_file("README.md","Create README.md",readmetext)