from flask import Blueprint, render_template

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
 return render_template("posts/create.html")

@bp.route("/posts")
def posts():
 list_of_posts = []
 return render_template("posts/posts.html", posts=list_of_posts)