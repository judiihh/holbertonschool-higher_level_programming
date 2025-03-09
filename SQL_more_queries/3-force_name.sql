-- This script creates the table force_name with id and a non-null name column.
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
