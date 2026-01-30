<<<<<<< HEAD
# Trade Tracker

Web-based stock portfolio management system with real-time tracking and transaction capabilities.  

## Live Demo

**Check out the live application**: [TradeTracker on PythonAnywhere](https://tanishquppal221.pythonanywhere.com/)

## Key Features

- **Stock Transactions**: Buy/sell shares with real-time price validation  
- **Portfolio Management**: Track holdings with automatic profit/loss calculations  
- **User Authentication**: Secure login/registration with password hashing  
- **Transaction History**: Permanent record of all trades with timestamps  
- **Real-time Quotes**: Integration with Yahoo Finance API for market data  
- **Input Validation**: Robust checks for share quantities and symbol validity  

## Tech Stack  

**Languages**:

- Python 3.9+  
- SQL  

**Database**:

- SQLite (file-based)  

**Frameworks**:

- Flask  
- Flask-Session  

**Libraries**:

- YFinance (for stock data)
- Requests (API integration)  
- Werkzeug (security)  

## Deployment

This application is deployed on PythonAnywhere, a cloud platform designed to host, run, and code Python in the cloud.

- **Live URL**: [https://tanishquppal221.pythonanywhere.com/](https://tanishquppal221.pythonanywhere.com/)
- **Deployment Date**: June 20, 2025
- **Platform**: PythonAnywhere

## Installation Guide

1. **Prerequisites**:  
   - Python 3.9+  
   - pip package manager  

2. **Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:

   ```bash
   flask run  # Automatically initializes database on first run
   ```

## Data Management

**Database Schema**:

| Table       | Columns                          | Constraints               |
|-------------|----------------------------------|---------------------------|
| users       | id, username, hash, cash        | Primary Key, Unique       |
| portfolio   | user_id, symbol, shares, total  | Foreign Key, Non-negative |
| transactions| user_id, symbol, shares, price  | Timestamped               |

**Validation Rules**:

- Share quantities must be positive integers  
- Stock symbols must validate against financial API  
- Usernames must be unique  
- Password minimum length: 8 characters  

## API Documentation

**Endpoints**:

```http
GET /quote?symbol={SYMBOL}
```

**Response Format**:

```json
{
  "name": "Company Name",
  "price": 150.75,
  "symbol": "SYM"
}
```

## Security Implementation

- Password hashing with PBKDF2-HMAC-SHA256  
- Session management with Flask-Session  
- CSRF protection through Flask-WTF (implied)  
- Input sanitization for all form fields  

## Error Handling

- Custom error pages for 400/500 responses  
- Database rollback on transaction failures  
- Graceful API failure handling  

## Contributing Guidelines

1. **Branching Strategy**:  
   - Feature branches from `main`  
   - PR reviews required before merging  

2. **Code Standards**:  
   - PEP8 compliance  
   - Type hints for complex functions  
   - Docstrings for all public methods  
=======
# Trade Tracker

Web-based stock portfolio management system with real-time tracking and transaction capabilities.  

## Live Demo

**Check out the live application**: [TradeTracker](https://tradetracker-9xi9.onrender.com/)

## Key Features

- **Stock Transactions**: Buy/sell shares with real-time price validation  
- **Portfolio Management**: Track holdings with automatic profit/loss calculations  
- **User Authentication**: Secure login/registration with password hashing  
- **Transaction History**: Permanent record of all trades with timestamps  
- **Real-time Quotes**: Integration with Yahoo Finance API for market data  
- **Input Validation**: Robust checks for share quantities and symbol validity  

## Tech Stack  

**Languages**:

- Python 3.9+  
- SQL  

**Database**:

- SQLite (file-based)  

**Frameworks**:

- Flask  
- Flask-Session  

**Libraries**:

- YFinance (for stock data)
- Requests (API integration)  
- Werkzeug (security)  

## Deployment

This application is deployed on OnRnder, a cloud platform designed to host, run, and code Python in the cloud.

- **Live URL**: [https://tradetracker-9xi9.onrender.com/](https://tradetracker-9xi9.onrender.com/)
- **Deployment Date**: June 20, 2025
- **Platform**: OnRender

## Installation Guide

1. **Prerequisites**:  
   - Python 3.9+  
   - pip package manager  

2. **Dependencies**:

   ```bash
     uv sync
   ```

3. **Database Setup**:

   ```bash
   flask run  # Automatically initializes database on first run
   ```

## Data Management

**Database Schema**:

| Table       | Columns                          | Constraints               |
|-------------|----------------------------------|---------------------------|
| users       | id, username, hash, cash        | Primary Key, Unique       |
| portfolio   | user_id, symbol, shares, total  | Foreign Key, Non-negative |
| transactions| user_id, symbol, shares, price  | Timestamped               |

**Validation Rules**:

- Share quantities must be positive integers  
- Stock symbols must validate against financial API  
- Usernames must be unique  
- Password minimum length: 8 characters  

## API Documentation

**Endpoints**:

```http
GET /quote?symbol={SYMBOL}
```

**Response Format**:

```json
{
  "name": "Company Name",
  "price": 150.75,
  "symbol": "SYM"
}
```

## Security Implementation

- Password hashing with PBKDF2-HMAC-SHA256  
- Session management with Flask-Session  
- CSRF protection through Flask-WTF (implied)  
- Input sanitization for all form fields  

## Error Handling

- Custom error pages for 400/500 responses  
- Database rollback on transaction failures  
- Graceful API failure handling  

## Contributing Guidelines

1. **Branching Strategy**:  
   - Feature branches from `main`  
   - PR reviews required before merging  

2. **Code Standards**:  
   - PEP8 compliance  
   - Type hints for complex functions  
   - Docstrings for all public methods  
>>>>>>> 9cf48b113ef3241f7a71ad778b75f9c6b8f63f35
