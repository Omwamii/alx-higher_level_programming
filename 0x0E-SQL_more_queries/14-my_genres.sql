-- script that uses `hbtn_0d_tvshows1 to list all genres of the show `Dexter`
SELECT tv_genres.name
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = 8
ORDER BY tv_genres.name;
