import os
import re
import random
import string

from datetime import date, timedelta
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required,verify_answer, create_email

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


@app.route("/")
@login_required
def index():
    # Erase games that have been created two days after
    game_ids = db.execute("SELECT game_id,date FROM actif_games")
    
    if game_ids != []:
        for i in range(len(game_ids)):
            if int(game_ids[i]["date"][:2]) + 1 < int(date.today().strftime("%d/%m/%Y")[:2]):
                rows = db.execute("DELETE FROM actif_players WHERE game_id = ?", game_ids[i]["game_id"])
                rows = db.execute("DELETE FROM question_for_game WHERE game_id = ?", game_ids[i]["game_id"])
                rows = db.execute("DELETE FROM actif_games WHERE game_id = ?", game_ids[i]["game_id"])

    return render_template("index.html",)

@app.route("/joingame", methods=["GET", "POST"])
@login_required
def joingame():
    
    # Ensure username was submitted
    if request.method == "POST":

        if not request.form.get("game_code"):
            return apology("donner le code du jeu", 401)

        # Redirect user to game page
        gamecode = request.form.get("game_code")
        return redirect("/games/" + gamecode)

    else:
        return render_template("joingame.html",)


@app.route("/games/<gamecode>/admin", methods=["GET", "POST"])
@login_required
def admingame(gamecode):

    # Find game_id via sqlite3 by 'selecting' from the database kraken the 'game_id'...
    # ... from the table 'actif_games' where gamecode equals the one in the url (variable 'gamecode')
    # The '?' fills in for a variable outside of the request which will be inserted into the line when it runs.
    game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", gamecode)

    if request.method == "POST":

        # Update database for actif_question 0 - first question
        rows = db.execute("UPDATE actif_games SET actif_question = 0")

        # Update users 'progress' to the first question
        players = db.execute("UPDATE actif_players SET progress = 0 WHERE game_id = ?", game_id[0]["game_id"])

        # Update users 'scores' to 0
        players = db.execute("UPDATE actif_players SET score = 0 WHERE game_id = ?", game_id[0]["game_id"])

        # Redirect user to game page
        return redirect("/games/" + gamecode)

    else:
        # Insert user into database - same line of code as before
        player_exists = db.execute("SELECT user_id FROM actif_players WHERE game_id=?", game_id[0]["game_id"])
        
        # Variable used to check if player is already in the game
        player_same = False

        # Iterates over all the players in game and changes the variable 'player_same' to true if the players is in the game
        for user in player_exists:
            if session["user_id"] == int(user["user_id"]):
                player_same = True
                break
        
        # If the player is not in the game, player_same == False, so the player is inserted into the database
        if player_same == False:
            rows = db.execute("INSERT INTO actif_players (user_id, game_id, score, progress) VALUES (?, ?, ?, ?)", session["user_id"], game_id[0]["game_id"], "0", "-1")

        
        # Check if game code is valid
        if game_id == []:
            return apology("Code de Jeu incorrect", 401)
        
        game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", gamecode)
        player_id = db.execute("SELECT user_id FROM actif_players WHERE game_id = ?", game_id[0]["game_id"])
        players = []
        for i in range(len(player_id)):
           players += db.execute("SELECT username FROM users WHERE id = ?", player_id[i]["user_id"])

        return render_template("admin.html", players=players, gamecode=gamecode)

@app.route("/games/<gamecode>", methods=["GET", "POST"])
@login_required
def game(gamecode):

    # Find game_id
    game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", gamecode)

    # Check if game code is valid
    if game_id == []:
        return apology("Code de Jeu incorrect", 404)
    
    # Find status of game
    game_progress = db.execute("SELECT actif_question FROM actif_games WHERE game_id = ?", game_id[0]["game_id"])
    # If not progress:
    if game_progress == []:
        return apology ("Une erreur s'est produite lors de la récupération de la progression du jeu, veuillez réessayer", 403)

    # Find time for the question
    time = db.execute("SELECT time_for_each_question FROM actif_games WHERE game_code = ?", gamecode)
    if time == []:
        return apology ("Something went wrong when retrieving the maximum time per question, please try again", 403)

    
    if int(game_progress[0]["actif_question"]) == -1:
            
            player_exists = db.execute("SELECT user_id FROM actif_players WHERE game_id=?", game_id[0]["game_id"])
            
            # Temporary variable to see if the current player is already in the list of players/in the database
            player_same = False

            # Goes over all of the players to check if current player is not in it
            for user in player_exists:
                if session["user_id"] == int(user["user_id"]):
                    player_same = True
                    break

            # Inserts player into database if he is new
            if player_same == False:
                rows = db.execute("INSERT INTO actif_players (user_id, game_id, score, progress) VALUES (?, ?, ?, ?)", session["user_id"], game_id[0]["game_id"], "0", "-1")
            return  render_template("game.html", progress = game_progress[0]["actif_question"], time = "2")

    # Find player progress
    player_progress = db.execute("SELECT progress FROM actif_players WHERE game_id = ? and user_id = ?", game_id[0]["game_id"], session["user_id"])
    # If not progress:
    if player_progress == []:
        return apology ("Une erreur s'est produite lors de la récupération du temps maximum par question, veuillez réessayer", 403)

    # Number of questions in game
    number_of_questions_in_game = db.execute("SELECT number_of_questions FROM actif_games WHERE game_id = ?", game_id[0]["game_id"])
    if number_of_questions_in_game == []:
        return apology ("Une erreur s'est produite lors de la récupération du nombre de questions dans le jeu, veuillez réessayer", 403)


    # Find player score
    score = db.execute("SELECT score FROM actif_players WHERE user_id = ? and game_id = ?", session["user_id"], game_id[0]["game_id"])
    if score == []:
        return apology ("Une erreur s'est produite lors de la récupération du score du joueur, veuillez réessayer", 403)
    
    score = int(score[0]["score"])

    # If the game has started, find question, check if the game is over, update score as needed, update question
    if game_progress[0]["actif_question"] != -1:

        # Find the current question id for game
        question_id = db.execute("SELECT question_id FROM question_for_game WHERE game_id = ? and question_number = ?", game_id[0]["game_id"], player_progress[0]["progress"])

        # When finished, lead to another page with the results
        if question_id == []:
            
            if request.method == "POST":
                # Find score for last question
                previous_question_id = db.execute("SELECT question_id FROM question_for_game WHERE game_id = ? and question_number = ?", game_id[0]["game_id"], int(number_of_questions_in_game[0]["number_of_questions"])-1)
            
                # Find answer
                answer = request.form["answer"]

                # Verify answer and update score
                score = verify_answer(previous_question_id[0]["question_id"], game_id[0]["game_id"], session["user_id"], score, answer)

            # Update player progress to finish
            rows = db.execute("UPDATE actif_players SET progress = ? WHERE user_id = ? and game_id=?", int(player_progress[0]["progress"])+1, session["user_id"], game_id[0]["game_id"])


            return redirect("/games/" + gamecode + "/results")

        # See if answer is correct
        if request.method == "POST":

            # Find the previous question that was answered
            previous_question_id = db.execute("SELECT question_id FROM question_for_game WHERE game_id = ? and question_number = ?", game_id[0]["game_id"], int(player_progress[0]["progress"])-1)

            #Find answer
            answer = request.form["answer"]

            #Verify answer and update score
            score = verify_answer(previous_question_id[0]["question_id"], game_id[0]["game_id"], session["user_id"], score, answer)


        # Update current question
        rows = db.execute("UPDATE actif_players SET progress = ? WHERE user_id = ? and game_id=?", int(player_progress[0]["progress"])+1, session["user_id"], game_id[0]["game_id"])
        rows = db.execute("UPDATE actif_games SET actif_question = ? WHERE game_code=?", int(game_progress[0]["actif_question"])+1, gamecode)

        # Select question
        question = db.execute("SELECT question, answer1, answer2, answer3, answer4, correct_answer FROM questions WHERE id = ?", question_id[0]["question_id"])

        # If not question, send error message
        if question == []:
            return apology ("Une erreur s'est produite lors de la récupération de la question, veuillez réessayer", 403)


    return render_template("game.html", progress = player_progress[0]["progress"], 
                                        question = question[0]["question"], 
                                        answer1=question[0]["answer1"], 
                                        answer2=question[0]["answer2"], 
                                        answer3=question[0]["answer3"], 
                                        answer4=question[0]["answer4"],
                                        number_of_questions_in_game = number_of_questions_in_game[0]["number_of_questions"],
                                        gamecode = gamecode,
                                        score = score,
                                        time = time[0]["time_for_each_question"])


@app.route("/games/<gamecode>/results", methods=["GET", "POST"])
@login_required
def results(gamecode):

    # Find game_id
    game = db.execute("SELECT game_id,number_of_questions FROM actif_games WHERE game_code = ?", gamecode)

    # Check if game code is valid
    if game == []:
        return apology("Code de Jeu Incorrect", 404)
    
    # Find players and their scores
    players = db.execute("SELECT user_id,score,progress FROM actif_players WHERE game_id = ?", game[0]["game_id"])
    # If not players:
    if players == []:
        return apology ("Une erreur s'est produite lors de la recherche des joueurs, veuillez réessayer", 403)


    usernames = []

    for i in range(len(players)):
        username = db.execute("SELECT username FROM users WHERE id = ?", players[i]["user_id"])
        # If not players:
        if username == []:
            return apology ("Une erreur s'est produite lors de la recherche du nom d'utilisateur, veuillez réessayer", 403)

        # See if player is still playing
        if players[i]["progress"] > int(game[0]["number_of_questions"]):
            progress = "a fini"
        else:
            progress = "est encore en train de jouer"

        username = username[0]["username"]
        usernames.append({"username": username, "score": players[i]["score"], "progress": progress})

    return render_template("results.html", usernames = usernames, gamecode = gamecode)

@app.route("/games/<gamecode>/correction")
@login_required
def correction(gamecode):
    
    # Find game_id
    game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", gamecode)

    # Check if game code is valid
    if game_id == []:
        return apology("il y a eu un problème pour trouver l'identifiant du jeu", 404)
    
    # Find questions and their answers
    question_ids = db.execute("SELECT question_id FROM question_for_game WHERE game_id = ?", game_id[0]["game_id"])
    # If not players:
    if question_ids == []:
        return apology ("Une erreur s'est produite lors de la recherche des joueurs, veuillez réessayer", 403)

    questions = []

    for i in range(len(question_ids)):
        # Find text and answer for each question
        question = db.execute("SELECT question, answer1, answer2, answer3, answer4, correct_answer FROM questions WHERE id = ?", question_ids[i]["question_id"])
        answer_id = str("answer" + question[0]["correct_answer"])
        answer = db.execute("SELECT ? FROM questions WHERE id = ?", answer_id, question_ids[i]["question_id"])

        questions.append({"question": question[0]["question"], "answer": question[0][answer_id]})

    return render_template("correction.html", questions = questions)

@app.route("/creategame", methods=["GET", "POST"])
@login_required
def creategame():
    if request.method == "POST":

        # Ensure number of questions was submitted
        if not request.form.get("subject"):
            return apology("sujet manquant", 401)
        subject = request.form.get("subject")

        # Ensure number of questions was submitted
        if not request.form.get("number_of_questions"):
            return apology("nombre de questions manquant", 401)
        number_of_questions = request.form.get("number_of_questions")

        # Ensure number of questions is between 1 and 15
        if int(number_of_questions) < 1 or int(number_of_questions) > 16:
            return apology( "Le nombre de questions doit être entre 2 et 15", 401)


        # Ensure time was submitted
        if not request.form.get("time"):
            return apology("temps manquant", 401)
        time = request.form.get("time")

        # Ensure time is between 5 and 20 seconds
        if int(time) < 2 or int(time) > 21:
            return apology( "Le timer doit être entre 3 et 20 secondes", 401)

        # Randomly generate game code
        letters = string.ascii_uppercase
        game_code = ''.join(random.choice(letters) for i in range(6))

        # Store information
        rows = db.execute("INSERT INTO actif_games (user_id, game_code, date, master, actif_question, time_for_each_question, subject, number_of_questions) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", session["user_id"], game_code, date.today().strftime("%d/%m/%Y"), True, "-1", time, subject, number_of_questions)
        
        # Fill in question_for_games table to have the questions for the new game

        game_id = db.execute("SELECT game_id FROM actif_games WHERE game_code = ?", game_code)
        question_id = db.execute("SELECT id FROM questions WHERE subject = ? ORDER BY RANDOM() LIMIT ?", subject, number_of_questions)
        if question_id == []:
            return apology ("désolé il y a eu un problème pour récupérer les questions", 403)

        for i in range (len(question_id)):
            rows = db.execute("INSERT INTO question_for_game (game_id, question_number, question_id) VALUES (?, ?, ?)", game_id[0]["game_id"], i, question_id[i]["id"])


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
            return apology("Identifiant manquant", 401)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Mot de Passe manquant", 401)


        # Query database for username
        username = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(username) != 1 or not check_password_hash(username[0]["hash"], request.form.get("password")):
            return apology("Identifiant et/ou Mot de Passe Incorrect", 401)

        # Remember which user has logged in
        session["user_id"] = username[0]["id"]

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




@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Identifiant Incorrect", 401)
        
        # Ensure username is not already in use
        username = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if username != []:
            return apology("Identifiant déjà existant", 401)
        
        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("Mot de Passe manquant", 401)

        # Ensure second password was submitted and is the same as first
        elif not request.form.get("confirmation"):
            return apology("nouveau mot de passe manquant ou non identique", 401)

        # Ensure password is strong
        elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', request.form.get("password")):
            return apology("Mot de Passe trop faible"), 401
        elif not re.search(r"\d", request.form.get("password")) and not re.search(r"[A-Z]", request.form.get("password")):
            return apology("Mot de Passe trop faible", 401)


        # Check if passwords are the same
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("Les deux Mots de Passe doivent être identiques", 401)

        # Store information
        rows = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(password))

        # Get user_id
        user_id = db.execute("SELECT id FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = user_id[0]["id"]

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