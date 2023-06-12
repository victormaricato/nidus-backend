DROP DATABASE IF EXISTS `nidus`;
CREATE DATABASE `nidus`;
USE `nidus`;

CREATE TABLE `user` (
    `id` VARCHAR(255) NOT NULL,
	`phone` VARCHAR(255),
    `tw_id` VARCHAR(255) NOT NULL,
    `tw_name` VARCHAR(255),
    `tw_access_token` VARCHAR(255) NOT NULL,
    `tw_access_token_verifier` VARCHAR(255) NOT NULL,
    `tw_profile_picture` VARCHAR(255),
    `tw_email` VARCHAR(100) DEFAULT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `settings` (
    `id` VARCHAR(255) NOT NULL,
    `user_id` VARCHAR(255) NOT NULL,
    `note` BOOLEAN NOT NULL DEFAULT TRUE,
    `task` BOOLEAN NOT NULL DEFAULT TRUE,
    `reminder` BOOLEAN NOT NULL DEFAULT TRUE,
    `email` BOOLEAN NOT NULL DEFAULT TRUE,
    `push` BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (`id`),
    KEY `settings_user_fk` (`user_id`),
    CONSTRAINT `settings_user_fk` FOREIGN KEY (`user_id`)
        REFERENCES `user` (`id`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `session` (
    `id` VARCHAR(255) NOT NULL,
    `user_id` VARCHAR(255) NOT NULL,
    `access_token` VARCHAR(255) NOT NULL,
    `active` BOOLEAN NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `end_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `session_user_fk` (`user_id`),
    CONSTRAINT `session_user_fk` FOREIGN KEY (`user_id`)
        REFERENCES `user` (`id`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `notes` (
    `id` VARCHAR(255) NOT NULL,
    `tweet_id` VARCHAR(255),
    `user_id` VARCHAR(255) NOT NULL,
    `content` VARCHAR(300) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `notes_user_fk` (`user_id`),
    CONSTRAINT `notes_user_fk` FOREIGN KEY (`user_id`)
        REFERENCES `user` (`id`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `reminders` (
    `id` VARCHAR(255) NOT NULL,
    `tweet_id` VARCHAR(255),
    `user_id` VARCHAR(255) NOT NULL,
    `content` VARCHAR(300) NOT NULL,
    `date` DATETIME NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `reminders_user_fk` (`user_id`),
    CONSTRAINT `reminders_user_fk` FOREIGN KEY (`user_id`)
        REFERENCES `user` (`id`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `tasklists` (
    `id` VARCHAR(255) NOT NULL,
    `tweet_id` VARCHAR(255),
    `user_id` VARCHAR(255) NOT NULL,
    `content` VARCHAR(300) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `tasklists_user_fk` (`user_id`),
    CONSTRAINT `tasklists_user_fk` FOREIGN KEY (`user_id`)
        REFERENCES `user` (`id`)
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `tasks` (
    `id` VARCHAR(255) NOT NULL,
    `tasklist_id` VARCHAR(255) NOT NULL,
    `complete` BOOL NOT NULL DEFAULT FALSE,
    `content` VARCHAR(300) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `tasks_tasklists_fk` (`tasklist_id`),
    CONSTRAINT `tasks_tasklists_fk` FOREIGN KEY (`tasklist_id`)
        REFERENCES `tasklists` (`id`) ON DELETE CASCADE
)  ENGINE=INNODB DEFAULT CHARSET=UTF8MB4;