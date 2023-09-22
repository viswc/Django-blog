sudo apt update
sudo apt install -y python3-pip nginx git
cd /blog
sudo pip3 install -r requirements.txt
cd /blog/Intern-blog
python3 manage.py collectstatic --noinput
nohup python3 manage.py runserver &

rm -f /etc/nginx/sites-enabled/default
cp /blog/nginx.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx