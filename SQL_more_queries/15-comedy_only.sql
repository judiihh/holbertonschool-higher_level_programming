-- Lists all comedy shows in the hbtn_0d_tvshows database
SELECT title FROM tv_shows
JOIN (
    tv_show_genres JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
) ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy"
ORDER BY title;
