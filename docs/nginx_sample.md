```
server {
    listen 44443 ssl;
    http2 on;
    server_name  movies.areslab.win;
    # access_log  /var/log/nginx/host.access.log  main;

    location / {
        # proxy_pass http://unix:/home/andrew/moviedb/movies.sock;
        proxy_pass http://127.0.0.1:8080;
    }

    location /static/ {
        # root /var/www;
        alias /var/www/static/;
    }
}
```