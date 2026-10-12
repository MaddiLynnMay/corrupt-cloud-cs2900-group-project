------------------------------------------------------------
-- This file not needed for program, I've just been using it
-- to write and test queries more easily.
------------------------------------------------------------

-- Ten transactions
SELECT * FROM AccTransaction LIMIT 10;

-- Biggest credit transaction
SELECT u.name, a.acc_name, t.date, MAX(t.amount), t.note
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
;

-- Biggest debit transaction
SELECT u.name, a.acc_name, t.date, MIN(t.amount), t.note
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
;

-- All transactions, sorted by amount
SELECT * FROM AccTransaction ORDER BY amount DESC;

-- sorted average transaction amount by account
SELECT u.name, a.acc_name, ROUND(AVG(t.amount)) AS average_transaction_amount
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
GROUP BY a.acc_name
ORDER BY average_transaction_amount DESC
;

-- sorted average transaction amount by user
SELECT u.name, ROUND(AVG(t.amount)) AS average_transaction_amount
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
GROUP BY u.ID
ORDER BY average_transaction_amount DESC
;

-- Get all account names for a given user name
SELECT u.name, a.acc_name
FROM Account a
JOIN User u ON u.ID = a.userID
WHERE u.name = 'Aragorn';

-- All transactions on given Account by account name
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.acc_name = "Strider's Checking"
ORDER BY date DESC;

-- All transactions on given Account by account ID
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.ID = 4
ORDER BY date DESC;

-- Recent 5 transactions on given Account by account name
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.acc_name = "Strider Checking"
ORDER BY date DESC
LIMIT 5;

-- HACKED all transactions on given Account
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.acc_name = "" OR 1=1-- Strider's Checking"
ORDER BY date DESC;

-- Recent 5 transactions on given Account by account ID
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.ID = 4
ORDER BY date DESC
LIMIT 5;

-- Get all user data
SELECT * FROM User;

-- Get user by username and password
SELECT *
FROM User
WHERE username = 'TheWhiteWizard' AND p_word = 'Fo0lOf4T0ok!';

-- HACKED1 Get user by username and password
SELECT *
FROM User
WHERE username = '' OR 1=1--' AND p_word = 'I'm hacking this query';

-- All transactions for given user name, ordered by date
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE u.name = 'Aragorn'
ORDER BY date;

-- Sum of all account balances by user's name
SELECT u.name, SUM(a.balance) AS "user_balance"
FROM User u
JOIN Account a ON a.userID = u.ID
WHERE u.name = "Aragorn"
GROUP BY u.ID;

-- Sum of all account balances by user ID
SELECT u.name, SUM(a.balance) AS "user_balance"
FROM User u
JOIN Account a ON a.userID = u.ID
WHERE u.ID = 2
GROUP BY u.ID;


-- Account balance by accountID
SELECT acc_name, balance
FROM Account
WHERE ID = 3;

-- Account balance by account name
SELECT acc_name, balance
FROM Account
WHERE acc_name = 'Greybeard Travel Funds';

-- get an account by it's name
SELECT *
FROM Account
WHERE acc_name = 'Aragorn Stash';

-- get an account by it's ID
SELECT *
FROM Account
WHERE ID = 5;

