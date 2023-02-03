import os
import re
import smtplib
import random
import string

from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, create_email

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///kraken.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    return render_template("index.html",)

@app.route("/jouer")
@login_required
def jouer():

    return render_template("jouer.html",)

@app.route("/joingame", methods=["GET", "POST"])
@login_required
def joining_game():
    
    # Ensure username was submitted
    if request.method == "POST":

        # TODO: perfect code number
        if not request.form.get("game_code"):
            return apology("must provide game code", 403)

        # TODO: finish page
        # Redirect user to game page
        gamecode = request.form.get("game_code")
        return redirect("/games/" + gamecode)

    else:
        return render_template("joingame.html",)


@app.route("/games/<gamecode>/admin", methods=["GET", "POST"])
@login_required
def admingame(gamecode):
    if request.method == "POST":

        # Update database for actif_question 1
        rows = db.execute("UPDATE actif_games SET actif_question = 0")

        # Redirect user to game page
        return redirect("/games/" + gamecode)
    else:
        # Find game_id
        game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", gamecode)

        # Check if game code is valid
        if game_id == []:
            # TODO: improve experience 
            return apology("Incorrect game code", 403)

        game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", gamecode)
        player_id = db.execute("SELECT user_id FROM actif_players WHERE game_id = ?", game_id[0]["game_id"])
        players = []
        for i in range(len(player_id)):
            players += db.execute("SELECT username FROM users WHERE id = ?", player_id[0]["user_id"])

        return render_template("admin.html", players=players)

@app.route("/games/<gamecode>")
@login_required
def joingame(gamecode):
    # Find game_id
    game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", gamecode)

    # Check if game code is valid
    if game_id == []:
        # TODO: improve experience 
        return apology("Incorrect game code", 403)

    # Insert into database new player
    player_exists = db.execute("SELECT user_id FROM actif_games WHERE game_code=?", gamecode)
    players_found = False
    for user in player_exists:
        if session["user_id"] != int(user["user_id"]):
            players_found=True
            rows = db.execute("INSERT INTO actif_players (user_id, game_id, score, progress) VALUES (?, ?, ?, ?)", session["user_id"], game_id[0]["game_id"], "0", "-1")
            break

    # Find status of game
    progress = db.execute("SELECT actif_question FROM actif_games WHERE game_code = ?", gamecode)
    #if not progress:
        #pass
        #TODO : handle that case 
    
    # Find questions for games
    subject = db.execute("SELECT subject FROM actif_games WHERE game_code = ?", gamecode)
    questions = db.execute("SELECT question FROM questions WHERE subject = ?", subject[0]["subject"])
    id = db.execute("SELECT id FROM questions WHERE subject = ?", subject[0]["subject"])
    answers = db.execute("SELECT answer FROM answers WHERE question_id = ?", id[0]["id"])

    return render_template("game.html", questions=questions, answers = answers)



@app.route("/creategame", methods=["GET", "POST"])
@login_required
def creategame():
    if request.method == "POST":
        # TODO : prepare for errors

        subject = request.form.get("subject")
        number_of_questions = request.form.get("number_of_questions")
        time = request.form.get("time")
        # Randomly generate game code
        letters = string.ascii_uppercase
        game_code = ''.join(random.choice(letters) for i in range(6))

        # Store information
        rows = db.execute("INSERT INTO actif_games (user_id, game_code, date, master, actif_question, question_time_stamp, time_for_each_question, subject, number_of_questions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", session["user_id"], game_code, datetime.now(), True, "-1", datetime.now(), time, subject, number_of_questions)
        
        return redirect("/games/" + game_code + "/admin")

    else:
        return render_template("creategame.html",)

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

        # TODO : fix bug where username is already taken
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/contacteznous", methods=["GET", "POST"])
@login_required
def contactez_nous():

    if request.method == "POST":

        # Ensure first_name was submitted
        if not request.form.get("first_name"):
            return apology("must provide first_name", 403)

        # Ensure last_name was submitted
        elif not request.form.get("last_name"):
            return apology("must provide last_name", 403)
        
        # Ensure email was submitted
        elif not request.form.get("email"):
            return apology("must provide email", 403)
            
        # Ensure idea was submitted
        elif not request.form.get("idea"):
            return apology("must provide idea", 403)
        
        # Send email with information from form
        send_from = os.environ["google_smtp_user"]
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(send_from , os.environ["google_smtp_password"])
            server.sendmail(send_from, send_from, create_email(
                 request.form.get("first_name"), request.form.get("last_name"), request.form.get("email"),
                 request.form.get("idea"), send_from))
        except: 

            return apology("Sorry, something went wrong")
        finally: 
            server.quit()

        return redirect("/")
    else:
        return render_template("contacteznous.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        
        # Ensure username is not already in use
        username = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if request.form.get("username") == username:
            return apology("username already exists")
        
        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure second password was submitted and is the same as first
        elif not request.form.get("confirmation"):
            return apology("must provide password again")

        # Ensure password is strong
        #elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', request.form.get("password")):
            #return apology("choose a stronger password")
        


        # Check if passwords are the same
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("both passwords must be identical")

        # Store information
        rows = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(password))

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("register.html")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)