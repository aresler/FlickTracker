#!/bin/bash

docker compose run web bash -c "python manage.py migrate && python manage.py collectstatic"
