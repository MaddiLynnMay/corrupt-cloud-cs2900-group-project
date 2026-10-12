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

-- All transactions on given Account
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.acc_name = "Strider's Checking"
ORDER BY date DESC;

-- Recent 5 transactions on given Account
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.acc_name = "Strider's Checking"
ORDER BY date DESC
LIMIT 5;

-- HACKED all transactions on given Account
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE a.acc_name = "" OR 1=1-- Strider's Checking"
ORDER BY date DESC;

-- Get all user data
SELECT * FROM User;

-- Get ID and name given a particular username and password
SELECT ID, name
FROM User
WHERE username = 'SamwiseTheBrave' AND p_word = '4myOldGaff3r!';

-- HACKED1 Get ID and name given a particular username and password
SELECT ID, name
FROM User
WHERE username = '' OR 1=1--' AND p_word = 'I'm hacking this query';

-- All transactions for given user name, ordered by date
SELECT a.acc_name, t.*
FROM AccTransaction t
JOIN Account a ON a.ID = t.accountID
JOIN User u ON u.ID = a.userID
WHERE u.name = 'Aragorn'
ORDER BY date;


