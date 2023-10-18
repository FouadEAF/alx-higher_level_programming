-- Script that create a table in MySQL server
-- Query to create the table in your MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
       id INT UNIQUE DEFAULT 1,
       name VARCHAR(256)
);
