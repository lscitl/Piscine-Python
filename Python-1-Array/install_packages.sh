#!/bin/sh

if [ ! -e ./bin/activate ]; then
    ~/goinfre/.brew/bin/python3.10 -m venv ./
fi

source ./bin/activate

pip install flake8 tqdm toml Pillow numpy matplotlib