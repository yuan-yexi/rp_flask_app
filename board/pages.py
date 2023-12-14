from flask import Blueprint

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return "Homepage"

@bp.route("/about")
def about():
    return "About"
