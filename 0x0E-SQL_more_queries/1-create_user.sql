-- Script that create an user in MySQL server
-- Query to create the user 'user_0d_1' in your MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
