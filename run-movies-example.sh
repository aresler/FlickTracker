docker run --rm -it --name movies \
	-v /home/andrew/projects/moviedb:/app \
	-v /etc/letsencrypt:/etc/letsencrypt \
	-v /home/andrew/projects/moviedb/nginx.prod:/etc/nginx/sites-enabled \
	-v /opt/moviedb/logs:/var/log/nginx/ \
	-p 8444:8444 \
	movies /bin/bash -c "service nginx start && \
		gunicorn --workers 1 --bind unix:/app/movies.sock --env DJANGO_SETTINGS_MODULE=moviedb.settings.prod moviedb.wsgi"
	#movies python /app/manage.py runserver 0:8000 --insecure
