-- create users table

DROP TABLE IF EXISTS users;
CREATE TABLE users (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, email varchar(255) NOT NULL UNIQUE, name varchar(255),  country CHAR(2) NOT NULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN')));

