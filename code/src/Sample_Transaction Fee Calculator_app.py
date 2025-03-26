from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Mock user credentials (Replace with DB check in production)
USERS = {"admin": "password123"}

EXCHANGE_RATES = {
    "USD_EUR": 0.92,
    "USD_GBP": 0.78,
    "EUR_USD": 1.09,
    "GBP_USD": 1.28
}

PROCESSING_FEES = {"USD": 2.5, "EUR": 2.2, "GBP": 2.0}
REGULATORY_FEE_PERCENT = 0.01

def calculate_transaction(amount, from_currency, to_currency):
    key = f"{from_currency}_{to_currency}"
    rate = EXCHANGE_RATES.get(key)
    
    if not rate:
        return {"error": "Exchange rate not available"}
    
    converted_amount = amount * rate
    processing_fee = PROCESSING_FEES.get(from_currency, 2.5)
    regulatory_fee = amount * REGULATORY_FEE_PERCENT
    total_fees = processing_fee + regulatory_fee
    final_amount = converted_amount - total_fees
    
    return {
        "converted_amount": converted_amount,
        "exchange_rate": rate,
        "processing_fee": processing_fee,
        "regulatory_fee": regulatory_fee,
        "total_fees": total_fees,
        "final_amount": final_amount
    }

@app.route('/')
def home():
    if "user" in session:
        return redirect(url_for("index"))
    return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        if USERS.get(username) == password:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password")
    
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/index')
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template('index.html')

@app.route('/calculate_fee', methods=['POST'])
def calculate_fee():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 403
    
    data = request.json
    amount = float(data.get("amount", 0))
    from_currency = data.get("from_currency")
    to_currency = data.get("to_currency")
    
    if amount <= 0:
        return jsonify({"error": "Invalid transaction amount"}), 400
    
    result = calculate_transaction(amount, from_currency, to_currency)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
