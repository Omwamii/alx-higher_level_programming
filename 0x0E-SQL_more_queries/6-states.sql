-- script to create db hbtn_0d_usa and table states in it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);