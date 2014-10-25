#!/bin/bash

rm README.md 
mkdir -p bin docs utilities/test
touch .gitignore CHANGES.txt LICENSE.txt MANIFEST.in README.txt setup.py bin/structure_package.sh utilities/__init__.py utilities/test/__init__.py
chmod -R o-rwx .[a-zA-Z]*
chmod -R g-rwx .[a-zA-Z]*
chmod -R o-rwx [a-zA-Z]*
chmod -R g-rwx [a-zA-Z]*

