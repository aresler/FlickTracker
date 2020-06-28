#!/bin/bash

backup_dir="/opt/moviedb/backups"

full_dump_file="full_dump.json"
app_dump_file="movies_dump.json"
current_date=$(date +"%Y-%m-%d")
docker exec \
	-e DJANGO_SETTINGS_MODULE="moviedb.settings.prod" \
	movies python /app/manage.py dumpdata > $full_dump_file

docker exec \
	-e DJANGO_SETTINGS_MODULE="moviedb.settings.prod" \
	movies python /app/manage.py dumpdata movies > $app_dump_file

tar -czvf $backup_dir/moviedb-dumps-${current_date}.tar.gz $full_dump_file $app_dump_file
rm $full_dump_file $app_dump_file