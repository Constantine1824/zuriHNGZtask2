#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

cd task2

python manage.py makemigrations
python manage.py migrate
cd ..