-- File: models/transformed/active_users.sql
SELECT 
    movie_id ,
    name AS users_name,
    COUNT(_id) AS count_comments
FROM
    comments
GROUP BY movie_id , users_name

