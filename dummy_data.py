from collections import namedtuple


users = set()
User = namedtuple('User', ['ID', 'name', 'username', 'p_word'])
users.add(User(1, "Samwise", "SamwiseTheBrave", "4myOldGaff3r!"))
users.add(User(2, "Aragorn", "IsildursHeir", "Uh4vMySw0rd"))
users.add(User(3, "Gandalf", "TheWhiteWizard", "Fo0lOf4T0ok!"))


accounts = set()
Account = namedtuple('Account', ['ID', 'userID', 'acc_name', 'balance'])
accounts.add(Account(1, 1, "Samwise Checking", 281))
accounts.add(Account(2, 2, "Strider Checking", 140))
accounts.add(Account(3, 2, "Aragorn Stash", 520))
accounts.add(Account(4, 2, "Treasury of the King", 56940))
accounts.add(Account(5, 3, "Mithrandir Savings", 2800))
accounts.add(Account(6, 3, "Greybeard Travel Funds", 640))


transactions = set()
Transaction = namedtuple('Transaction', ['ID', 'accountID', 'date', 'amount', 'balance', 'note'])

# ============================================================
# Samwise's Checking
# ============================================================
transactions.add(Transaction(1, 1, "3019-03-13", -3, 278,
    "Potatoes and other provisions purchased in Hobbiton"))
transactions.add(Transaction(2, 1, "3019-03-15", -2, 276,
    "Seed packets and gardening supplies"))
transactions.add(Transaction(3, 1, "3019-03-18", -5, 271,
    "Travel provisions for the journey"))
transactions.add(Transaction(4, 1, "3019-03-19", -1, 270,
    "Rope and other camping supplies"))
transactions.add(Transaction(5, 1, "3019-03-25", -4, 266,
    "Bread, cheese, and provisions purchased on the road"))
transactions.add(Transaction(6, 1, "3019-04-01", -3, 263,
    "Gardening tools and seeds for rebuilding Bag End"))
transactions.add(Transaction(7, 1, "3019-04-03", 25, 288,
    "Payment received for helping restore the Shire"))
transactions.add(Transaction(8, 1, "3019-04-10", -7, 281,
    "Pipe-weed and Hobbiton provisions"))

# ============================================================
# Strider's Checking
# ============================================================
transactions.add(Transaction(9, 2, "3018-10-01", -15, 193,
    "Horse feed and supplies purchased in Bree"))
transactions.add(Transaction(10, 2, "3018-10-02", -8, 185,
    "Room and meals at the Prancing Pony"))
transactions.add(Transaction(11, 2, "3018-10-03", -12, 173,
    "Travel supplies and provisions"))
transactions.add(Transaction(12, 2, "3018-10-04", -20, 153,
    "Repairs and supplies for travel"))
transactions.add(Transaction(13, 2, "3018-10-25", -10, 143,
    "Provisions purchased near Rivendell"))
transactions.add(Transaction(14, 2, "3018-12-25", -18, 125,
    "Travel supplies purchased before departing Rivendell"))
transactions.add(Transaction(15, 2, "3019-01-15", -25, 100,
    "Horse care and provisions"))
transactions.add(Transaction(16, 2, "3019-03-20", 40, 140,
    "Payment received for services rendered while traveling"))

# ============================================================
# Aragorn's Stash
# ============================================================
transactions.add(Transaction(17, 3, "3018-10-06", -30, 390,
    "Weapons maintenance and repairs"))
transactions.add(Transaction(18, 3, "3018-10-20", -45, 345,
    "Supplies and equipment for the journey"))
transactions.add(Transaction(19, 3, "3018-12-20", -25, 320,
    "Travel equipment and cold-weather provisions"))
transactions.add(Transaction(20, 3, "3019-02-10", -35, 285,
    "Horse supplies and equipment"))
transactions.add(Transaction(21, 3, "3019-03-01", -50, 235,
    "Replacement equipment and provisions"))
transactions.add(Transaction(22, 3, "3019-04-15", 125, 360,
    "Reward received for service to Gondor"))
transactions.add(Transaction(23, 3, "3019-05-01", -40, 320,
    "Personal travel expenses after the War"))
transactions.add(Transaction(24, 3, "3019-06-15", 200, 520,
    "Payment from the royal household"))

# ============================================================
# The King's Treasury
# ============================================================
transactions.add(Transaction(25, 4, "3019-05-02", 2500, 54690,
    "Tax revenue collected from Gondor"))
transactions.add(Transaction(26, 4, "3019-05-05", -750, 53940,
    "Reconstruction of Minas Tirith"))
transactions.add(Transaction(27, 4, "3019-05-12", -350, 53590,
    "Food and supplies distributed to citizens"))
transactions.add(Transaction(28, 4, "3019-05-20", 1800, 55390,
    "Royal revenue from trade"))
transactions.add(Transaction(29, 4, "3019-06-01", -1200, 54190,
    "Military equipment and repairs"))
transactions.add(Transaction(30, 4, "3019-06-15", -500, 53690,
    "Rebuilding roads and public infrastructure"))
transactions.add(Transaction(31, 4, "3019-07-01", 3200, 56890,
    "Taxes and trade revenue"))
transactions.add(Transaction(32, 4, "3019-07-15", -850, 56040,
    "Funding for rebuilding the city"))
transactions.add(Transaction(33, 4, "3019-08-01", -600, 55440,
    "Royal household expenses"))
transactions.add(Transaction(34, 4, "3019-08-15", 1500, 56940,
    "Trade revenue from allied kingdoms"))

# ============================================================
# Mithrandir's Savings
# ============================================================
transactions.add(Transaction(35, 5, "3018-08-01", -20, 2880,
    "Fireworks and supplies for Hobbiton celebrations"))
transactions.add(Transaction(36, 5, "3018-09-20", -15, 2865,
    "Pipe-weed purchased from Hobbiton"))
transactions.add(Transaction(37, 5, "3018-10-01", -35, 2830,
    "Travel supplies and provisions"))
transactions.add(Transaction(38, 5, "3018-12-01", -50, 2780,
    "Books and research materials"))
transactions.add(Transaction(39, 5, "3019-01-10", -30, 2750,
    "Supplies for an extended journey"))
transactions.add(Transaction(40, 5, "3019-03-25", -75, 2675,
    "Horse and travel expenses"))
transactions.add(Transaction(41, 5, "3019-04-10", 150, 2825,
    "Payment received for consulting and services"))
transactions.add(Transaction(42, 5, "3019-05-05", -25, 2800,
    "Books and scholarly materials"))

# ============================================================
# Greybeard's Travel Funds
# ============================================================
transactions.add(Transaction(43, 6, "3018-09-01", -10, 655,
    "Travel provisions"))
transactions.add(Transaction(44, 6, "3018-09-15", -15, 645,
    "Horse feed and stable fees"))
transactions.add(Transaction(45, 6, "3018-10-20", -20, 625,
    "Lodging and meals during travels"))
transactions.add(Transaction(46, 6, "3018-11-01", -12, 613,
    "Replacement walking staff"))
transactions.add(Transaction(47, 6, "3018-12-20", -25, 588,
    "Travel supplies before departing Rivendell"))
transactions.add(Transaction(48, 6, "3019-01-15", -18, 570,
    "Provisions and supplies"))
transactions.add(Transaction(49, 6, "3019-03-10", -30, 540,
    "Emergency travel expenses"))
transactions.add(Transaction(50, 6, "3019-04-20", 100, 640,
    "Reimbursement for supplies provided to the Fellowship"))

