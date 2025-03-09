-- This script creates the table unique_id with an id column that must be unique and has a default value of 1, and a name column.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
