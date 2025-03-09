-- This script lists all genres from hbtn_0d_tvshows with the number of shows linked to each.
SELECT g.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_show_genres AS tsg
JOIN genres AS g ON tsg.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
