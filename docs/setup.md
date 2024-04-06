# Setup

> [!NOTE]
> *This document serves the purpose of showing how the project was initially set up for development.*

## Initialize Repository

```bash
# create github remote repository
gh repo create noclocks/template-crewai-langchain --public -d 'CrewAI + Langchain Template Project' --clone .

# change directory
cd template-crewai-langchain

# set python version via pyenv
pyenv local 3.12.0

# initialize python via poetry
poetry init -n
poetry shell

# add git files
touch .gitignore .gitattributes

# add readme, changelog, and license
touch README.md CHANGELOG.md LICENSE.md

# add folders
mkdir docs
mkdir src
mkdir tests

# install dependencies



```
