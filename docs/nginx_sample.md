```
server {
	listen 8000;
	server_name  localhost;

	location / {
		proxy_pass http://unix:/app/movies.sock;
	}

	location /static/ {
		alias /app/static/;
	}
}
```