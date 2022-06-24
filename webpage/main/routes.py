from flask import render_template, Blueprint
from webpage.models import Post
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/feed")
def feed():
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template('feed.html', posts=posts)

