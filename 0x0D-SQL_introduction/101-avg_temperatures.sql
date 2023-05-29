-- script that imports a table from another file and displays avg temp
-- display values
SELECT `city`, AVG(`value`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
