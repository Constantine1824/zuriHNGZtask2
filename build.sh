#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install


task2/python manage.py makemigrations
task2/python manage.py migrate