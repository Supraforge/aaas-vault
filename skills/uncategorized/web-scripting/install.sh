#!/bin/bash
# Installation script for web-scripting skill

echo "Installing dependencies for web-scripting skill..."

# Check if we're on a Debian-based system
if [ -f /etc/debian_version ]; then
    echo "Debian-based system detected. Using apt-get..."
    
    # Update package list
    apt-get update
    
    # Install Ruby
    if ! command -v ruby &> /dev/null; then
        echo "Installing Ruby..."
        apt-get install -y ruby
    else
        echo "Ruby is already installed."
    fi
    
    # Install PHP
    if ! command -v php &> /dev/null; then
        echo "Installing PHP..."
        apt-get install -y php
    else
        echo "PHP is already installed."
    fi
    
    # Install Rails (via gem)
    if ! command -v rails &> /dev/null; then
        echo "Installing Rails..."
        gem install rails
    else
        echo "Rails is already installed."
    fi
    
    # Install Composer
    if ! command -v composer &> /dev/null; then
        echo "Installing Composer..."
        php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
        php composer-setup.php --install-dir=/usr/local/bin --filename=composer
        php -r "unlink('composer-setup.php');"
    else
        echo "Composer is already installed."
    fi
    
else
    echo "Non-Debian system detected. Please install dependencies manually:"
    echo "- Ruby: https://www.ruby-lang.org/en/documentation/installation/"
    echo "- PHP: https://www.php.net/manual/en/install.php"
    echo "- Rails: gem install rails"
    echo "- Composer: https://getcomposer.org/download/"
fi

echo "✅ web-scripting skill dependencies installed."
