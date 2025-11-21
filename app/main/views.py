from flask import render_template
from flask_login import current_user
from . import main
from app.models import User

@main.route('/')
def index():
    users = None

    if current_user.is_authenticated:
        users = User.query.all()

    return render_template('index.html', users=users)