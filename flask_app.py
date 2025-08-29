from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

#Home
@app.route('/')
def index():
    current_time = datetime.utcnow()
    return render_template('index.html', current_time=current_time)

#User
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#Not found 404
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
