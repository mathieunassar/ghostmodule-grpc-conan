#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv

    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi

    python --version
    pyenv install 3.7.1
    pyenv virtualenv 3.7.1 conan

    pyenv rehash
    pyenv activate conan    
fi

pip install conan --upgrade
pip install conan_package_tools

conan user
