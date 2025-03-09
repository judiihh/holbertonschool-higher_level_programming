-- This script creates the table id_not_null with an id column that cannot be null and defaults to 1, and a name column.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
