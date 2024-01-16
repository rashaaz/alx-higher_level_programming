-- 10-top_score.sql
-- List all records of the second_table, ordered by score
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
