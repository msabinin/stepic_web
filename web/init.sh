#!/bin/bash
base_dir=${PWD}
nginx='sudo ln -s $base_dir/etc/nginx.conf /etc/nginx/sites-enabled/test.conf'
eval $nginx
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web
gunicorn hello:wsgi_app --bind 0.0.0.0:8080 &
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
sudo mysql -u root -e "create database stepic_web; create user box@localhost; grant all privileges on stepic_web.* to box@localhost with grant option;"
cd ask
python3 manage.py makemigrations qa
python3 manage.py migrate
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 &

