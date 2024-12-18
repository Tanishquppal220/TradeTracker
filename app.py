import os

from sql import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///New_Database.db")


def buy_sell(x):
    id = session["user_id"]
    # Retrive Symbol and No of shares
    symbol = request.form.get("symbol").upper()
    shares = request.form.get("shares")

    # check if symbol or shares field are not empty
    if not symbol:
        return apology("Enter a Valid symbol")

    if x == 1:
        # Check If shares is a intger
        if not shares.isdigit() or int(shares) < 0:
            return apology("Enter a numeric,non-fractional,non-negative shares")
    if x == -1:
        hold = db.execute("select shares from portfolio where user_id=? and symbol=?", id, symbol)
        if not shares.isdigit() or int(shares) < 0:
            return apology("Enter a numeric,non-fractional,non-negative shares")
        if hold[0]["shares"] < int(shares):
            return apology("You don't have that much shares")
    shares = int(shares)
    # Finds the share in market
    quote = lookup(symbol)

    # check if name of share actully exist or not
    if quote == None:
        return apology("Invalid symbol")

    # Price of that Share
    price = quote["price"]

    # cost to buy m no of share
    cost = price*shares  # always +Ve

    # uniqne id of logged in user

    # gets the cash user has
    buget = db.execute("SELECT cash FROM users WHERE id=?", id)[0]["cash"]
    if cost > buget and x == 1:
        return apology("Can't Afford")

    # record transaction
    db.execute("INSERT INTO transactions(user_id,symbol,shares,price) values(?,?,?,?)",
               id, symbol, shares*x, price)

    # get portfolio
    data = db.execute(
        f"select symbol,shares,total from portfolio where user_id={id}")

    # add to portfolio
    for i in data:
        print(i)
        if i["symbol"] == symbol:
            temp = i["shares"]+(shares*x)
            if temp == 0:
                db.execute(
                    "delete from portfolio where symbol=? and user_id=?", symbol, id)
                break
            else:
                temp_t = i["total"]+(cost*x)
                db.execute(
                    f"update portfolio set shares=? ,total=? where user_id=? and symbol=?", temp, temp_t, id, symbol)
                break
    else:
        db.execute("INSERT INTO portfolio(user_id,symbol,shares,price,total) values(?,?,?,?,?)",
                   id, symbol, shares, price, cost)
    # Deduct or add cash
    new_buget = buget - (cost*x)
    db.execute("update users set cash=? where id=?", new_buget, id)
    return 0


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    id = session["user_id"]
    data = db.execute(
        "select symbol,shares,price,total from portfolio where user_id=?", id)
    cash = db.execute("select cash from users where id=?", id)
    print(data)
    investment = 0
    for i in data:
        investment += i["total"]
    total = cash[0]["cash"] + investment
    return render_template("homepage.html", data=data, cash=cash[0]["cash"], total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        a = buy_sell(1)
        if a == 0:
            flash("Bought!")
            return redirect("/")
        else:
            return a
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    id = session["user_id"]
    l = db.execute("select * from transactions where user_id=?", id)
    print(l)
    return render_template("history.html", l=l)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get(
                "username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please enter a Valid symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol")
        quote["price"] = usd(quote['price'])

        return render_template("quoted.html", quote=quote)
    else:
        return render_template("quote.html")
    # return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        username = request.form.get("username")
        password1 = request.form.get("password")
        password2 = request.form.get("confirmation")
        if password1 == password2:
            password_hash = generate_password_hash(password1)
        else:
            return apology("Password is not correct")
        try:
            db.execute("insert into users(username,hash) values(?,?)",
                       username, password_hash)
        except:
            return apology("Username already exists")
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Registerd")
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        a = buy_sell(-1)
        if a == 0:
            flash("Sold!")
            return redirect("/")
        else:
            return a

    else:
        l = db.execute(
            "select symbol from portfolio where user_id=?", session["user_id"])
        print(l)
        return render_template("sell.html", list=l)


if __name__ == "__main__":
    app.run(debug=True)
