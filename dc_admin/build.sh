#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r dc_admin/requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate