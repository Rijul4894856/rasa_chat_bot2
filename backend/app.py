from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import bcrypt
import random
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Temporary in-memory OTP storage
otp_storage = {}

def connect_db():
    return sqlite3.connect("users.db")

def send_email_otp(email, otp):
    sender_email = "cipher72347538@gmail.com"  # Replace with your bot email
    sender_password = "ysil ukit czll twxa"     # Gmail App Password

    msg = MIMEText(f"Your OTP is: {otp}")
    msg["Subject"] = "Your OTP Code"
    msg["From"] = sender_email
    msg["To"] = email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"[✅] OTP sent to {email}")
    except Exception as e:
        print("[❌] Email sending failed:", e)

@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        email = data["email"]
        mobile = data["mobile"]

        if not username or not password or not email or not mobile:
            return jsonify({"success": False, "message": "All fields are required!"}), 400

        otp = str(random.randint(100000, 999999))
        otp_storage[username] = {"otp": otp, "data": data}

        send_email_otp(email, otp)

        return jsonify({"success": True, "message": "OTP sent to your email."})
    
    except Exception as e:
        print("Error in /signup:", e)
        return jsonify({"success": False, "message": "Signup failed due to server error."}), 500

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debugging line to see the incoming request

        username = data.get("username")
        user_otp = data.get("otp")

        # Check if username and otp are provided
        if not username or not user_otp:
            return jsonify({"success": False, "message": "Missing OTP or username"}), 400

        # Check if OTP matches the stored value
        if username in otp_storage and str(otp_storage[username]["otp"]) == str(user_otp):
            user_data = otp_storage[username]["data"]
            hashed_pw = bcrypt.hashpw(user_data["password"].encode('utf-8'), bcrypt.gensalt())

            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (username, password_hash, email, mobile) VALUES (?, ?, ?, ?)",
                    (user_data["username"], hashed_pw, user_data["email"], user_data["mobile"])
                )
                conn.commit()
                del otp_storage[username]
                return jsonify({"success": True, "message": "Registration successful!"})
            except sqlite3.IntegrityError as e:
                print(f"Database error: {e}")  # Log any database-related issues
                return jsonify({"success": False, "message": "Username already exists!"})
            finally:
                conn.close()

        return jsonify({"success": False, "message": "Invalid OTP!"})

    except Exception as e:
        print(f"Error in /verify-otp: {e}")  # Log any errors that happen in the try block
        return jsonify({"success": False, "message": "Server error during OTP verification."}), 500


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_hash = result[0].encode('utf-8') if isinstance(result[0], str) else result[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                return jsonify({"success": True, "message": "Login successful!"})

        return jsonify({"success": False, "message": "Invalid credentials!"})

    except Exception as e:
        print("Error in /login:", e)
        return jsonify({"success": False, "message": "Login failed due to server error."}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)
