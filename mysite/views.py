from flask import Blueprint, jsonify


views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def index():
    return jsonify({"hello": "world"})