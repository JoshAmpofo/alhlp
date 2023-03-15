-- This script will create a db `hbtn_0d_usa` and a table `states`
-- The table will have the desc:
--	`id` and `name`
-- `id` should be unique, autogenerated, not null an primary key
-- If db and table already exists, script should not fail


CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `states` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL, 
	PRIMARY KEY (`id`)
	);
