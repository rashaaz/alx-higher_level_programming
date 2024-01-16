-- 16-no_link.sql
-- List all records with a name value from second_table
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
