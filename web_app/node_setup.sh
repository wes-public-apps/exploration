# !/bin/bash

# Install nvm
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.bashrc

# Install node
nvm install node

# Install node dependencies
npm install -g create-react-app  # global context install
