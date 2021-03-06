import sqlite3
import random

DB_FILE="users.db"

def createTables():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = """CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        wins INTEGER NOT NULL,
        losses INTEGER NOT NULL,
        money INTEGER NOT NULL,
        timesBroke INTEGER NOT NULL)
    """
    c.execute(command)
    command = """CREATE TABLE IF NOT EXISTS games(
        gamecode INTEGER NOT NULL,
        gamestage TEXT NOT NULL,
        gamecards TEXT NOT NULL)
    """
    c.execute(command)
    db.commit()
    db.close()

createTables();

def addUser(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES(?, ?, 0, 0, 10000, 0)", (username, password))
    db.commit()
    db.close()


def makeLoginsDict():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT username, password FROM users")
    logininfo = c.fetchall()

    loginsinfo = {} # create a dictionary for all the login information

    for login in logininfo:
        loginsinfo[login[0]] = login[1]

    return loginsinfo
    db.close()

def checkUser(username):
    loginsinfo = makeLoginsDict()
    return username in loginsinfo.keys()

def checkPass(username, password):
    loginsinfo = makeLoginsDict()
    return (loginsinfo[username] == password)

def addProfile(ID):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO profiles VALUES(?, ?, ?, ?, ?)", (ID, 0, 0, 0, 0))
    db.commit()
    db.close()

def updateUserMoney(username, amount):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE users SET money = money + (?) WHERE username = (?)", (amount, username))
    db.commit()
    db.close()

def updateUserWin(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE users SET wins = wins + 1 WHERE username = (?)", (username,))
    db.commit()
    db.close()

def updateUserLoss(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE users SET losses = losses + 1 WHERE username = (?)", (username,))
    db.commit()
    db.close()

def getMoney(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT money FROM users WHERE username = (?)", (username,))
    money = c.fetchall()[0][0]
    db.close()
    return money

def addMoney(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT money FROM users WHERE username = (?)", (username,))
    money = c.fetchall()[0][0]
    if (money < 0):
        c.execute("UPDATE users SET money = 10000 WHERE username = (?)", (username,))
        c.execute("UPDATE users SET timesBroke = timesBroke + 1 WHERE username = (?)", (username,))
    db.commit()
    db.close()

def getRandomNumber(lower, upper, takens):
    randomNumber = random.randint(lower, upper)
    sortedTakens = takens.copy()
    sortedTakens.sort()
    for taken in sortedTakens:
        if randomNumber < taken:
            return getRandomNumber
        randomNumber += 1

def first(lst):
    return lst[0]

def getGamecodes():
    b = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT gamecode FROM games")
    gamecodes = list(map(first, c.fetchall()))
    db.close()
    return gamecodes

def addGame():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    gamecode = getRandomNumber(1000, 9999, getGamecodes())
    c.execute("INSERT INTO games VALUES (?, 0, '')")
    db.commit()
    db.close()
