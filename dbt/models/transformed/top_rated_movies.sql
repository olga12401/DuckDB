SELECT
    _id AS movie_id,
    title,
    genres,
    metacritic
FROM movies
WHERE metacritic IS NOT NULL
ORDER BY metacritic DESC
LIMIT 10;
