-- script that lists all cities of california that can be found in hbtn_0d_usa
SELECT states.id , cities.name
FROM cities, states
WHERE  cities.state_id =  states.id 
AND states.name = 'California'
ORDER BY cities.id ASC;
