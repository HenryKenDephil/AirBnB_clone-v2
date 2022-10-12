--setting MySQL setup for development
-- scripts that prepare mysql server fpr the project

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS `hbnb_dev`@'localhost' IDENTIFIED BY `hbnb_dev_pwd`;
USE hbnb_dev_db;
GRANT ALL PREVILEGES ON hbnb_dev_db.* To 'hbnb_dev'@'localhost';
GRANT SELECT PREVILIGES ON performance_schema.* To 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
