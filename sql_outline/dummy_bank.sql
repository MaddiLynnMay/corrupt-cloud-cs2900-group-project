-- This is the format for the dummy bank, we won't actually be
-- referencing this file though at all.

DROP DATABASE IF EXISTS dummy_bank;
CREATE DATABASE dummy_bank;
USE dummy_bank;

CREATE TABLE User (
    ID SMALLINT UNSIGNED PRIMARY KEY,
    name VARCHAR(50),
    username VARCHAR(50),
    p_word VARCHAR(50)
);

CREATE TABLE Account(
    ID SMALLINT UNSIGNED PRIMARY KEY,
    user_id SMALLINT UNSIGNED,
    acc_name VARCHAR(50,),
    balance DECIMAL(15,2)
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE Transaction(
    ID SMALLINT UNSIGNED PRIMARY KEY,
    account_id SMALLINT UNSIGNED,
    date DATETIME
    amount DECIMAL(15,2),
    balance DECIMAL(15,2),
    note VARCHAR(50),
    CONSTRAINT fk_account_id FOREIGN KEY (account_id) REFERENCES account(account_id)
);