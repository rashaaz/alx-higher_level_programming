-- 11-genre_id_all_shows.sql.
-- Using the hbtn_0d_tvshows database
-- Selecting shows with their corresponding genres
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
