#!/bin/bash
python manage.py collectstatic && gunicorn --workers 2 erp_backend.wsgi