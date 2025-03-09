-- List all records from second_table where the name column is not empty,
-- displaying score and name, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
