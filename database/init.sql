-- SQLBook: Code
CREATE DATABASE IF NOT EXISTS development_db;

USE development_db;

CREATE TABLE IF NOT EXISTS test_data (
    test_id CHAR(36) PRIMARY KEY,
    test_name VARCHAR(100) UNIQUE NOT NULL
);

SET @user1 = UUID();

INSERT INTO test_data (
    test_id, test_name
)

VALUES (
    @user1, 'Bob'
);
