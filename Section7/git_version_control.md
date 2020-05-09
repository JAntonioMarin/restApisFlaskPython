### Installing Git on Mac and Windows
- In my case ubuntu:
    `apt-get install git-core`

### What is a Git repository?

- git-scm.com

### The Git workflow (part 1)

- For initialize git repository: `git init`
- Status of repository: `git status`
- Create a file: `touch app.py`
- Commit: `git commit - "Created a simple Flask application"`

### The Git workflow (part 2)
- Create GITHUB account
- Create a new repository (choose Public or Private)
- Now push an existing repository from the command line:
    - `git remote add origin http://github.com/name/repository.git`
    - `git push --set-upstream origin master`
    - Put username and password

### Using SSH Keys for security (Optional)

- Create a ssh key: `ssh-keygen`
- Cat ssh key: `cat /Users/yourname/.ssh/id_rsa.pub`
- Copy on your github account > Profile > Edit your profile > SSH and GPG Keys, and add the key.
- In your repository in Clone or download active Use SSH.
- In your local branch put:
    - `git remote remove origin`
    - `git remote add origin git@github.com:youname/repository.git`



