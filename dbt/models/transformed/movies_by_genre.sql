SELECT
    genres,
    COUNT(*) AS movie_count
FROM movies
GROUP BY genres
ORDER BY movie_count DESC;
