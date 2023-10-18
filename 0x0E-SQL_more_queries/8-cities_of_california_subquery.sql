-- Script that list all the cities of California registered in DB
-- Query to list all the cities from California
SELECT id, name
FROM cities
-- Query to get the id of California
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California"
);
