-- Creating table unique_id if not exist with DEFAULT 1 UNIQUE
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
