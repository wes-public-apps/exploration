# !/bin/bash

# Install Rust Dependencies
sudo apt install build-essential -y

# Install Rust Tools
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
rustup component add rustfmt
