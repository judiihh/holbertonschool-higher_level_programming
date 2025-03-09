-- This script lists all Comedy shows in the hbtn_0d_tvshows database.
SELECT ts.title
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
JOIN genres AS g ON tsg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY ts.title ASC;
