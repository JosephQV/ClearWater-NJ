To run the code, run this in the terminal:

**python main.py**

The main.py file creates the kivy App instance and loads the component widgets and screens from every other file. You do not need to replicate
anything from main.py in the files you work on.

For setting up your python environment in a directory and installing the needed packages, see below. This also outlines the commands needed for creating a new git branch and pushing your changes to it. Please ask about this if you are confused.

# Environment Setup #
If you have an empty directory that you plan to work in for this project,
running these commands will setup a Python 'venv' virtual environment and
install the kivy package. It will then basically link this local directory
to the remote project repository on GitHub by cloning it (downloading the files
from GitHub and storing copies of them here).

**Run one at a time in this order.**

This will clone the project repository from GitHub to the local directory you are
open to in the terminal. From now on, work directly in this cloned folder. The next 
command will switch to it in the terminal.

**git clone https://github.com/JosephQV/GSSTeam12Project.git**


cd is 'change directory'. The subsequent path is the folder where the terminal will be open to.

**cd GSSTeam12Project**


This uses the standard Python venv package (virtual environment) to create a virtual environment
that is just named '.venv' in the current directory. If you want to call it something else,
replace the last part ('.venv') with your preferred environment name like 'my_env'. Note that
you will also need to change this for the next command if you do.

**python -m venv .venv**

The next command runs the activate script created in the venv to activate the virtual environment
in the terminal so that whenever you do 'pip install ...' or 'python ...' you will be installing
the packages to your environment or running your code in the context of the environment so that it
can find and import any needed packages from it. You should see some indication in your terminal
that the environment has been activated after running this.
Note: this is operating system specific because the structure of the venv and the file type of the 
activate script are different for different OS.
Also note: **This is the only command from this environment setup you will need to re-run whenever you work on the project.**

ON WINDOWS:

**.\.venv\Scripts\activate.ps1**

ON MAC:

**source .venv/bin/activate**

This installs the kivy package used for making apps with Python. Ensure you have activated
your virtual environment (previous command) before running it so that kivy is installed there.

**pip install kivy**

For installing other packages:

**pip install pandas**

etc.


# git Commands #
Useful git command to see whats going on (staged changes, waiting commits, current branch, etc.)

**git status**

To create a git branch to work on and then switch to it. Replace branch name as needed.

**git branch "branch name"**

**git switch "branch name"**


To see all branches on your local repository.

**git branch**


To share your code to the GitHub repository using git - 3 steps:

This is called 'staging' your changes. Do this for each file you want to include in a single
commit before running git commit.

**git add file.py**

This is committing your changes with a required message.

**git commit -m "Added blah blah blah"**

This pushes (uploads) your commit(s) to the GitHub repository linked to your local.

**git push**

When the remote repository updates as others make changes, you can run:

**git fetch**
to update your local without making changes to it yet. This will just tell git where your
local repository is behind or different from the remote. 

To integrate the changes into your local code, run:

**git pull**

^On master branch in your local repository.

You will need to do git pull occaisonally when changes are made on the remote that need to be
pulled in your code.

You might have to run this command as well.
On your branch that you are working on, run

**git merge master**

to update everything.
