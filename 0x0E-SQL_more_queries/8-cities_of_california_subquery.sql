-- script that lists all cities of california that can be found in hbtn_0d_usa
SELECT states.id , cities.name
FROM hbtn_0d_usa.states, hbtn_0d_usa.cities
WHERE  cities.state_id = 1
ORDER BY cities.id ASC;
