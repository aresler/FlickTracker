#!/bin/bash

#gunicorn -w 1 -b :8080 moviedb.wsgi
gunicorn -w 1 -b unix:/app/movies.sock moviedb.wsgi

# Possible options:
# --access-logfile gunicorn.log
