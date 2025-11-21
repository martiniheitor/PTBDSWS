from flask import render_template
from flask_login import login_required
from . import main
from app.models import User

@main.route('/')
@login_required
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)