--a script that prepares MySQL serer for the project
--creating  hbnb_test_db_database
--proiding previleges to new user(hbnb_test)

CREATE DATABASE IF NOT EXISTS 'hbnb_test_db';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
USE hbnb_test_db;
GRANT ALL PREVILEGES ON hbnb_test_db.* To 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* To 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;