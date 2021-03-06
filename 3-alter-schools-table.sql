/*
Write an SQL file here, which changes the schools table's schema with the followings:
- adds an address field (varchar), without the NOT NULL constraint
- modifies the 'name' column's name to 'code'
*/

ALTER TABLE schools ADD address VARCHAR;
ALTER TABLE schools RENAME COLUMN name TO code;