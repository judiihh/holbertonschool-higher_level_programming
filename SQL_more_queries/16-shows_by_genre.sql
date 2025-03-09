-- This script lists all shows and all genres linked to that show from the hbtn_0d_tvshows database.
SELECT ts.title, g.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
LEFT JOIN genres AS g ON tsg.genre_id = g.id
ORDER BY ts.title ASC, g.name ASC;

