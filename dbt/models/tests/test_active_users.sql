-- Test: Ensure no user has a negative comment count
SELECT *
FROM {{ ref('active_users') }}
WHERE comment_count < 0;
