-- This script lists all cities from the database hbtn_0d_usa with the format: cities.id - cities.name - states.name.
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
