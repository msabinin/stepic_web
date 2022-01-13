#!/bin/bash
base_dir=${PWD}
nginx='sudo ln -s $base_dir/etc/nginx.conf /etc/nginx/sites-enabled/test.conf'
eval $nginx
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web
gunicorn hello:wsgi_app --bind 0.0.0.0:8080 &
cd ask
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 &
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
