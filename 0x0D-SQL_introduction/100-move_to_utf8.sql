-- script to convert hbtn_0c_0 database, first_table and field 'name'  to UTF8 in server

-- convert database to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;

-- convert table to utf8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert field 'name' to utf8
ALTER TABLE first_table MODIFY COLUMN `name` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci;
