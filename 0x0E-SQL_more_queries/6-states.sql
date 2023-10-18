-- Script that create a DB and a table in
-- Query to create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Query to create state table in new DB
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
