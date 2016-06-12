#!/bin/bash

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VIRTUALENV_ROOT="$BASEDIR/env"

source "$VIRTUALENV_ROOT/bin/activate"

if [ ! -d $VIRTUALENV_ROOT ]; then
    VIRTUALENV=`which virtualenv`
    echo "Creating virtualenv..."
    "$VIRTUALENV" "$VIRTUALENV_ROOT" --python=python3 > /dev/null
    source "$VIRTUALENV_ROOT/bin/activate"
    pip install -r "$BASEDIR/requirements.txt"
fi

PYTHON_VERSION=`python -c 'import sys; print(sys.version_info[0])'`

if [ "$PYTHON_VERSION" -lt "3"  ]; then
    source "$VIRTUALENV_ROOT/bin/activate"
fi

python $BASEDIR/manage.py db upgrade

exit 0

echo "Starting URLShortener"

exec gunicorn app:app \
--pythonpath $APPDIR \
-b 0.0.0.0:5000
