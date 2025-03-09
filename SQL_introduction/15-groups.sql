-- List the number of records for each score in second_table,
-- displaying the score and the count of records (labeled as 'number'),
-- sorted by the number of records in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
