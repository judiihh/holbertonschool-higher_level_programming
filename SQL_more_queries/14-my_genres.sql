-- This script lists all genres of the show Dexter from the hbtn_0d_tvshows database.
SELECT g.name
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
JOIN genres AS g ON tsg.genre_id = g.id
WHERE ts.title = 'Dexter'
ORDER BY g.name ASC;
