#!/bin/bash

VIRTUALENV=`which virtualenv`
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VIRTUALENV_ROOT="$BASEDIR/env"

if [ -z "$POSTGRESQL_DATABASE" ]; then
    echo "The environment variable 'POSTGRESQL_DATABASE' not found or is empty."
    echo "Use the command:"
    printf "\texport POSTGRESQL_DATABASE=\"postgresql://username:password@host:port/database\"\n"
    echo "ex:"
    printf "\texport POSTGRESQL_DATABASE=\"postgresql://scott:tiger@localhost/mydatabase\"\n"
    exit -1
fi

if [ -z "$VIRTUALENV" ]; then
    echo "Installing virtualenv..."
    apt-get update
    apt-get install python-virtualenv -y
fi

# get include path for this python version
INCLUDE_PY=$(python3 -c "from distutils import sysconfig as s; print s.get_config_vars()['INCLUDEPY']")
if [ ! -f "${INCLUDE_PY}/Python.h" ]; then
    apt-get install python3-dev -y
fi

