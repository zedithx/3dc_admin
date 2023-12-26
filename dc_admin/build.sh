#!/usr/bin/env bash
# exit on error
set -o errexit

cd dc_admin

python manage.py collectstatic --no-input
python manage.py migrate
pip install -r requirements.txt

