-- script that lists all shows fro `hntn_0d_tvshows_rate` by rating
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings 
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
