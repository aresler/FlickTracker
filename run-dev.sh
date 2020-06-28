if [[ "$(docker image inspect movies 2>/dev/null)" == "[]" ]]; then
	docker build -t movies .
fi

docker run --rm -it --name movies \
	-v /Users/Andrey.Resler/myprojects/moviedb:/app \
	-v /Users/Andrey.Resler/myprojects/moviedb/nginx.dev:/etc/nginx/sites-enabled \
	-v /tmp/moviedb/logs:/var/log/nginx/ \
	-p 8000:8000 \
	movies /bin/bash -c "service nginx start && \
		gunicorn --workers 1 --bind unix:/app/movies.sock --env DJANGO_SETTINGS_MODULE=moviedb.settings.dev moviedb.wsgi"

	# movies bash -c "export DJANGO_SETTINGS_MODULE=moviedb.settings.dev; bash"
	#movies python /app/manage.py runserver 0:8000 --insecure
