#!/usr/bin/env bash
# This sets up your web servers for the deployment of web_static

apt-get -y update
apt-get -y install nginx

ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

service nginx restart
