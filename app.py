import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, Response
from flask_session import Session
from tempfile import mkdtemp
import random
from helpers import apology, login_required

''' 
Initializes all the nedeed applications to run my code on the top 
some of the finance PSET code was used here for login and
apology 
'''
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///wellness.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache",
    return response

    
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or rows[0]["password"] != request.form.get("password"):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/")
@login_required
def index():
    return taskVisualizer()


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# creates a new entry in the user table, renders apology if forms are not filled properly
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        users = db.execute("SELECT username FROM users")
        if not request.form.get("username") or not request.form.get("password"):
            return apology("Please fill both your username and password.", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Please confirm your password.", 400)
        for name in users:
            if name["username"] == request.form.get("username"):
                return apology("Username already exists, please try another one", 400)
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", request.form.get("username"), request.form.get("password"))
        return render_template("success.html")
    return render_template("register.html")


# Adds a new row to the tasks table where other functions of the website can read out from
@app.route("/createTask", methods=["GET", "POST"])
def taskmaker():
    if request.method == "POST":
        if request.form.get("create-task"):
            newTask = request.form.get("create-task")
            db.execute("INSERT INTO tasks(task, userId, date, complete) VALUES (?, ?, ?, ?)", newTask, session["user_id"], datetime.datetime.now(), 0)
    return taskVisualizer()


@app.route("/deleteTask", methods=["GET", "POST"])
def taskDeleter():
    if request.method == "POST":
        if request.form.get("delete-task"):
            taskDel = request.form.get("delete-task")
            db.execute("DELETE FROM tasks WHERE task = ? AND userId = ?", taskDel, session["user_id"]) 
        return taskVisualizer()
    return taskVisualizer()


# Present all the tasks in a table and tells the user if they were completed or not
@app.route("/taskManager", methods=["GET", "POST"])
def taskVisualizer():
    tasks = db.execute("SELECT * FROM tasks WHERE userId = ?", session["user_id"])
    taskSuggestion = db.execute("SELECT * FROM tasks WHERE userId = 2")
    for task in tasks:
        if task["complete"] == None or task["complete"] == 0:
            task["complete"] = "Not completed yet"
        else:
            task["complete"] = "Completed!"
    return render_template("taskManager.html", tasks = tasks, taskSuggestion = taskSuggestion)

# Completes a single task
@app.route("/completeTask", methods=["GET", "POST"])
def completeTask():
    if request.method == "POST":
        if not request.form.get("confirm-task"):
            return apology("Please select a task to delete")
        db.execute("UPDATE tasks SET complete = 1 WHERE userId = ? AND task = ?;", session["user_id"], request.form.get("confirm-task"))
        return taskVisualizer()
    return taskVisualizer()

# Reset all existing tasks to not completed yet
@app.route("/resetTask", methods=["GET", "POST"])
def resetTask():
    if request.method == "POST":
        db.execute ("UPDATE tasks SET complete = 0 WHERE userId = ?", session["user_id"])
    return taskVisualizer()


# Takes a random quote from the dailymotivation table and sends out to the html page
@app.route("/dailyMotivation")
def daily():
    length = db.execute("SELECT MAX(textId) FROM dailyMotivation")
    print(length[0]["MAX(textId)"])
    luckyNumber = random.randint(1, length[0]["MAX(textId)"])
    selectedText = db.execute("SELECT text FROM dailyMotivation WHERE textId = ?", luckyNumber )
    return render_template("dailyMotivation.html", text = selectedText[0]['text'] )


# Allows the user to write entries into the diary table
@app.route("/diary", methods=["GET", "POST"])
def diary():
    if request.method == "POST":
        if not request.form.get("new-entry"):
            return apology("Please type something on your diary first")
        db.execute ("INSERT INTO diary(entry, date, userId) VALUES(?, ?, ?)", request.form.get("new-entry"), datetime.datetime.now(), session["user_id"])        
    diary = db.execute("SELECT * FROM diary WHERE userId = ?", session["user_id"])
    return render_template("diary.html", diary = diary )

