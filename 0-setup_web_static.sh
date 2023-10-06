#!/usr/bin/env bash
# Web servers for the deployment.

trap 'exit 0' ERR
if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"

html_file="<html>
  <head></head>
  <body>Holberton school</body>
</html>"

echo "$html_file" | sudo tee /data/web_static/releases/test/index.html > /dev/null

rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo wget -q -O /etc/nginx/sites-available/default http://exampleconfig.com/static/raw/nginx/ubuntu20.04/etc/nginx/sites-available/default
configuration="/etc/nginx/sites-available/default"
echo 'Holberton School Hello World!' | sudo tee /var/www/html/index.html > /dev/null
sudo sed -i '/^}$/i \ \n\tlocation \/redirect_me {return 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;}' $configuration
sudo sed -i '/^}$/i \ \n\tlocation @404 {return 404 "Ceci n'\''est pas une page\\n";}' $configuration
sudo sed -i 's/=404/@404/g' $configuration
sudo sed -i "/^server {/a \ \tadd_header X-Served-By $HOSTNAME;" $configuration
sudo sed -i '/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $configuration

sudo service nginx restart
