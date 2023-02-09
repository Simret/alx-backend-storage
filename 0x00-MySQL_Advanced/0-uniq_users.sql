-- create users table

CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, email varchar(255) NOT NULL UNIQUE, name varchar(255));

