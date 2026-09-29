```bash
mkdir ~/Projects/Mademoiselle
cd ~/Projects/Mademoiselle
mkdir frontend backend
cd backend

```
Afterwards we created a virtual environment where we downloaded django through the command `python -m pip install django`  we can further verify if it is downloaded by running a version check.

Next we moved to the frontend and tried to set up by checking for node and npm and while they were installed they were not up to date and so running `npm create vite@latest .` did not work so we upgraded the node by installing and making it the main node through the following commands.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.8/install.sh | bash
source ~/.bashrc
nvm install node
nvm alias default node
nvm use node
```

# Project Requirement
