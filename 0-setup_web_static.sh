#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
	apt-get -y update
	apt-get install -y nginx
fi

mkdir -p /data/web_static/{shared,releases/test}

# Create a test HTML file
cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>
EOF
# Remove the existing symbolic link if it exists and then create a new one
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data/ directory recursively
chown -R ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"
tmp_config_file="/etc/nginx/sites-available/default.tmp"

# Create a temporary config file with the updated Nginx configuration
cp "$config_file" "$tmp_config_file"
sed -i 's@^\(\s*root\s*\).*;\$@\1/data/web_static/current;@' "$tmp_config_file"

# Add the alias directive to the Nginx configuration
sed -i '/^\s*location \/ {/a \        location /hbnb_static/ {\n            alias /data/web_static/current/;\n        }' "$tmp_config_file"

# Replace the original config file with the updated one
mv "$tmp_config_file" "$config_file"

# Restart Nginx
service nginx restart
