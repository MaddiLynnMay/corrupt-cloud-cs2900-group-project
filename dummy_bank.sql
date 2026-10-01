DROP DATABASE IF EXISTS dummy_bank;
CREATE DATABASE dummy_bank;
USE dummy_bank;

CREATE TABLE user (
    user_id SMALLINT UNSIGNED PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE account(
    account_id SMALLINT UNSIGNED PRIMARY KEY,
    user_id SMALLINT UNSIGNED,
    amount DECIMAL(15,2)
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE Transaction(
    transaction_id SMALLINT UNSIGNED PRIMARY KEY,
    account_id SMALLINT UNSIGNED,
    amount DECIMAL(15,2),
    t_type ENUM('debit', 'credit')
    CONSTRAINT fk_account_id FOREIGN KEY (account_id) REFERENCES account(account_id)
);