import os
from flask import Flask, jsonify, make_response, redirect, request, session
from flask_cors import CORS
from dotenv import load_dotenv
from waitress import serve

#Get env variables
load_dotenv()

#Set up app with Flask
app = Flask(__name__)

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
APP_URL = os.getenv('APP_URL')
API_ACCESS_KEY = os.getenv('API_ACCESS_KEY')

#Configure Flask session for HTTPS hosting
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_SAMESITE"] = None  #Allows cross-site cookies
app.config["SESSION_COOKIE_SECURE"] = True  #Only over HTTPS
app.secret_key = FLASK_SECRET_KEY
CORS(app, supports_credentials=True, origins=[f"{APP_URL}"])

#Function to lock backend route calls without key
def require_api_key(f):
    def decorated_function(*args, **kwargs):
        api_key = request.args.get("api_key")
        if api_key != API_ACCESS_KEY:
            return jsonify({"error": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function

#Default path
@app.route("/", methods=["GET"])
def default_api():
    return jsonify({"message": "API is working!"})

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000, threads=6, debug=True, timeout=120)
