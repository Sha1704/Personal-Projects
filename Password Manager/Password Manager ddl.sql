Drop database if exists password_manager;
Create database password_manager;
use password_manager;

-- user table
CREATE TABLE user (
    Username VARCHAR(50) NOT NULL,
    master_password_hash VARCHAR(250) NOT NULL,
    encryption_key VARCHAR(250) NOT NULL,
    PRIMARY KEY (Username)
);

-- Account_Password table
CREATE TABLE Account_Password (
    account_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL,
    account_username VARCHAR(250) NOT NULL,
    encrypted_account_password VARCHAR(600) NOT NULL,
    url VARCHAR(250) NULL,
    notes VARCHAR(250) NULL,
    Nonce VARCHAR(600) NOT NULL,
    Tag VARCHAR(600) NOT NULL,
    PRIMARY KEY (account_name , Username),
    FOREIGN KEY (Username)
        REFERENCES user (username)
        ON DELETE CASCADE ON UPDATE CASCADE
);


