#!/usr/bin/env bash

DB_USER="hbnb_dev"
DB_PASSWORD="hbnb_dev_pwd"
DB_NAME="hbnb_dev_db"

# Run the SQL commands using the mysql client
mysql -u $DB_USER -p$DB_PASSWORD -e "USE $DB_NAME;
ALTER TABLE places
ADD COLUMN city_id VARCHAR(60) NOT NULL,
ADD CONSTRAINT fk_cities FOREIGN KEY (city_id) REFERENCES cities(id);"
