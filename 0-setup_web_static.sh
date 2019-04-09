#!/usr/bin/env bash
# Configures the server file system and install nginx
apt-get -q update
echo "installing nginx"
apt-get -qy install nginx
WH="/data/web_static"
mkdir -p $WH/releases/test/
mkdir -p $WH/shared/
printf "Hello, Holberton!" > $WH/releases/test/index.html
ln -sf $WH/releases/test $WH/current
chown -R ubuntu:ubuntu /data/

# Configure Nginx Server.

DEST="/etc/nginx"
src="/var/www/default"
Static="/var/www/default"
url="https://www.youtube.com/watch?v=QH2-TGUlwu4"
echo "server  {
	listen 80 default_server;
	listen [::]:80 default_server;
	server_name localhost;
	error_page 404 /page_not_found.html;
	root $Static;

	location / {
		index index.html index.html;	
	}

	location /redirect_me {
		return 301 $url;
	}

	location /hbnb_static/ {
		alias $WH/current/;
	}	

}" > "$DEST/sites-available/default"
mkdir -p $Static
echo "Holberton School was here!" > $Static/index.html
echo "Ceci n'est pas une page" > $src/page_not_found.html
header="add_header X-served-By \$hostname"
if ! grep -q "$header" $DEST/nginx.conf; 
then
	sed -i "/http {.*/a $header;" $DEST/nginx.conf
fi

service nginx restart
