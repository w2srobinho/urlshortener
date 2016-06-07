#!/bin/bash

VIRTUALENV=`which pyvenv`
APPDIR=$(dirname $(realpath "$0"))
VIRTUALENV_ROOT="$APPDIR/env"

if [ -z "$VIRTUALENV" ]; then
    echo "Installing Python3.5"    
    apt-get update
    apt-get install python3.5
    VIRTUALENV=`which pyvenv`
fi

if [ ! -d $VIRTUALENV_ROOT ]; then
    "$VIRTUALENV" "$VIRTUALENV_ROOT" > /dev/null
fi

source "$APPDIR/env/bin/activate"
pip install -r "$APPDIR/requirements.txt"

if [ -z "$POSTGRESQL_DATABASE" ]; then
    echo "The environment variable 'POSTGRESQL_DATABASE' not found or is empty."
    echo "Use the command:"
    printf "\texport POSTGRESQL_DATABASE=\"postgresql://username:password@host:port/database\"\n"
    echo "ex:"
    printf "\texport POSTGRESQL_DATABASE=\"postgresql://scott:tiger@localhost/mydatabase\"\n"
    exit -1
fi

python "$APPDIR/manager.py db upgrade"
