-- Test: All top-rated movies should have a metacritic score greater than 0
SELECT *
FROM {{ ref('top_rated_movies') }}
WHERE metacritic <= 0;
