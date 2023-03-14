-- This script will display max temps of each state in db
-- Results will be ordered by state name


SELECT `State`, MAX(`value`) AS `max_temp` FROM `temperatures`
GROUP BY `State` ORDER BY `STATE` ASC;
