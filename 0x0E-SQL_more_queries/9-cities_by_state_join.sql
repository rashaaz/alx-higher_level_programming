-- 9-cities_by_state_join.sql.
-- Using the hbtn_0d_usa database
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
