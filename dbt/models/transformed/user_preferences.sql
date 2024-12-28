SELECT
    name,
    preferences->'preferred_genre' AS preferred_genre,
    COUNT(*) AS activity_count
FROM users
WHERE preferences IS NOT NULL
GROUP BY name, preferred_genre
ORDER BY activity_count DESC;
