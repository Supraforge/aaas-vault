#!/bin/bash
# Install script for memory-safety-patterns skill

echo "Installing dependencies for memory-safety-patterns..."

# Update package list
echo "Updating package list..."
apt-get update -y

# Install C and C++ compilers
if ! command -v gcc &> /dev/null; then
    echo "Installing gcc..."
    apt-get install -y gcc
else
    echo "gcc already installed."
fi

if ! command -v g++ &> /dev/null; then
    echo "Installing g++..."
    apt-get install -y g++
else
    echo "g++ already installed."
fi

# Install Valgrind
if ! command -v valgrind &> /dev/null; then
    echo "Installing valgrind..."
    apt-get install -y valgrind
else
    echo "valgrind already installed."
fi

# Install Rust (if not present)
if ! command -v rustc &> /dev/null; then
    echo "Installing Rust..."
    curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source $HOME/.cargo/env
    echo "Rust installed. You may need to restart your shell or run \"source $HOME/.cargo/env\"."
else
    echo "Rust already installed."
fi

# Check for cargo
if ! command -v cargo &> /dev/null && command -v rustc &> /dev/null; then
    echo "Cargo might be missing. Ensure Rust is properly installed."
fi

echo "Dependency installation complete for memory-safety-patterns."
