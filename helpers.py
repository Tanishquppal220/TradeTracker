import requests

from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def lookup(symbol):
    """Look up quote for symbol using YFinance."""
    try:
        import yfinance as yf
        
        # Get the ticker information
        ticker = yf.Ticker(symbol.upper())
        
        # Get the latest market data
        ticker_data = ticker.info
        
        # Check if we got valid data
        if not ticker_data or "regularMarketPrice" not in ticker_data:
            print(f"No data found for symbol: {symbol}")
            return None
            
        # Some symbols might not have a long name, fall back to the symbol itself
        name = ticker_data.get("longName", ticker_data.get("shortName", symbol.upper()))
        
        # Extract the current price
        price = ticker_data.get("regularMarketPrice", 0.0)
        if price is None:
            price = ticker_data.get("currentPrice", 0.0)
        
        return {
            "name": name,
            "price": float(price),
            "symbol": symbol.upper()
        }
    except Exception as e:
        print(f"YFinance error: {e}")
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
