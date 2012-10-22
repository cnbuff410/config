#!/bin/bash

# Build
sudo apt-get install build-essential

# Python tools
sudo apt-get install python-pip python-dev python-setuptools
sudo easy_install pylint

# Latex
sudo apt-get install texlive

# Vim
sudo apt-get install vim vim-scripts vim-doc vim-latexsuite vim-gui-common vim-gnome

# Git
sudo apt-get install git
cp ./git_completion.bash ~/.git_completion.bash

# ctags
sudo apt-get install exuberant-ctags

