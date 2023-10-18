-- Script that list all cities contained in the DB
-- Query to join cities and states
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;
