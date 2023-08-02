from flask import Blueprint, jsonify


views = Blueprint("views", __name__)

@views.route("/", methods=["POST"])
def index():
    return jsonify({"hello": "world"})