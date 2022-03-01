#! /usr/bin/bash

echo "---------------- setting PYTHONPATH ----------------"
touch __init__.py
export PYTHONPATH=$PWD
echo "PYTHONPATH="$PYTHONPATH
echo "----------------------------------------------------"
