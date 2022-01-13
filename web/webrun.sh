#!/bin/bash
gunicorn -c gunicorn.py &
cd ./ask
gunicorn -c gunicorn_django.py &
