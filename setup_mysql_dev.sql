-- A script that prepares a MYSQL server for this project

-- This creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- This creates a new user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- This line grants all privileges to the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- This line grants SELECT privilege to the database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
