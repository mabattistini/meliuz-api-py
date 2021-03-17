#!/usr/bin/env bash

VENV="venv"
DBPATH="database"

if ! [ -d $VENV ] ; then
  virtualenv $VENV
fi

source $VENV/bin/activate

$VENV/bin/pip install -r requirements.txt

$VENV/bin/python migrate.py db init
$VENV/bin/python migrate.py db migrate
$VENV/bin/python migrate.py db upgrade

$VENV/bin/python $DBPATH/create_pokemons.py $DBPATH
