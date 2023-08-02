from flask import Blueprint, request, jsonify, json
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()



def token_required(f):
    wraps(f)
    def required(*args, **kwargs):
        return f(*args, **kwargs)
    return required


auth = Blueprint("auth", __name__)

@auth.route("/", methods=["POST"])
def home():
    if request.method == "POST":
        token = request.json["token"]
        data = jwt.decode(token, os.environ["SECRET_KEY"], algorithms="HS256")
        return jsonify(data)
    return jsonify({})



@auth.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.json["email"]
        password = request.json["password"]


        user = User.query.filter_by(email=email).first()
        if user:
            print(user.full_name)
            if check_password_hash(user.password, password):
                del user.password
                token = jwt.encode({
                    "first_name": user.full_name,
                    "phone_number": user.phone_number,
                    "email": user.email
                }, 
                # "expiration": str(datetime.utcnow() + timedelta(seconds=120))
                os.environ["SECRET_KEY"], algorithm="HS256")
                return jsonify({"token": token})
        return jsonify({})

@auth.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        full_name = request.json["full_name"]
        email = request.json["email"]
        phone_number = request.json["phone_number"]
        password1 = request.json["password1"]
        password2 = request.json["password2"]


        user = User.query.filter_by(email=email).first()

        if user:
            print(user)
            return jsonify({"msg": "User already exists with this email"})
        else:
            hashed_password = generate_password_hash(password1, method="sha256")
            new_user = User(email=email, password=hashed_password, full_name=full_name, phone_number=phone_number)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"msg": "success"})
    return jsonify({})

