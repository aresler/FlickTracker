#!/bin/bash

gunicorn -w 3 -b 0.0.0.0:8080 moviedb.wsgi
#gunicorn -w 1 -b unix:/app/movies.sock moviedb.wsgi

# Possible options:
# --access-logfile gunicorn.log
