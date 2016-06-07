#!/bin/bash

APPDIR=$(dirname $(realpath "$0"))
VIRTUALENV_ROOT="$APPDIR/env"

source "$APPDIR/env/bin/activate"

echo "Starting URLShortener"

exec gunicorn app:app \
--pythonpath $APPDIR \
-b 0.0.0.0:5000
