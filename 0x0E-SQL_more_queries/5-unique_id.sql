-- creates table 'unique_id' on server
-- create table , id being default of 1 and unique
CREATE TABLE IF NOT EXISTS `unique_id`(id INT UNIQUE DEFAULT 1, name VARCHAR(256));

