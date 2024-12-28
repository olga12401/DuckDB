-- Ensure that all movies have a non-zero comment count per user
SELECT *
FROM {{ ref('users_comments') }}
WHERE count_comments <= 0
