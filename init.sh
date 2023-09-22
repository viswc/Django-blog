#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
sudo apt update
sudo apt install -y python3-pip nginx git
cd /blog
sudo pip3 install -r requirements.txt
cd /blog/Intern-blog
python3 manage.py collectstatic --noinput
cp /blog/Intern-blog/compress/CACHE /blog/Intern-blog/static/
nohup python3 manage.py runserver &

rm -f /etc/nginx/sites-enabled/default
cp /blog/configuration/nginx.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx