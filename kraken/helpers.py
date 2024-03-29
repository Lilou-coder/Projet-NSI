from cs50 import SQL
from flask import redirect, render_template, session
from functools import wraps



# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///kraken.db")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", space=" ", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def verify_answer(question_id, game_id, user_id, score, answer):
    # Select question
    question = db.execute("SELECT correct_answer FROM questions WHERE id = ?", question_id)
    # If not question, send error message
    if question == []:
        return apology ("Something went wrong when retrieving the question, please try again", 403)

    # Check if answer is correct
    if answer == question[0]["correct_answer"]:
        score += 1
        rows = db.execute("UPDATE actif_players SET score = ? WHERE user_id = ? and game_id = ?", score, user_id, game_id)
    return score
