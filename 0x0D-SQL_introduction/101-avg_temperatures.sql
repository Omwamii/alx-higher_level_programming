-- script that imports a table from another file and displays avg temp
-- import the database
SOURCE temperatures.sql

-- display values
SELECT `city`, AVG(`value`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
