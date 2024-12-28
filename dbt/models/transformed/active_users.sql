SELECT
    name,
    COUNT(*) AS comment_count
FROM comments
GROUP BY name
ORDER BY comment_count DESC
LIMIT 10;
