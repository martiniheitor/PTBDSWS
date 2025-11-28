import os
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_prova_web'

# Configuração do Banco de Dados SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

# --- MODELOS (Banco de Dados) ---
class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    discipline = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<Professor {self.name}>'

# --- FORMULÁRIOS ---
class ProfessorForm(FlaskForm):
    name = StringField('Cadastre o novo Professor:', validators=[DataRequired()])
    discipline = SelectField('Disciplina associada:', choices=[
        ('DSWA5', 'DSWA5'),
        ('GPSA5', 'GPSA5'),
        ('IHCA5', 'IHCA5'),
        ('SODA5', 'SODA5'),
        ('PJIA5', 'PJIA5'),
        ('TCOA5', 'TCOA5')
    ], validators=[DataRequired()])
    submit = SubmitField('Cadastrar')


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/professores', methods=['GET', 'POST'])
def professores():
    form = ProfessorForm()
    if form.validate_on_submit():
        # Cria novo professor
        novo_professor = Professor(name=form.name.data, discipline=form.discipline.data)
        db.session.add(novo_professor)
        db.session.commit()
        flash('Professor cadastrado com sucesso!')
        return redirect(url_for('professores'))

    # Recupera todos os professores do banco para exibir na tabela
    todos_professores = Professor.query.all()
    return render_template('professores.html', form=form, professores=todos_professores)

# Rotas para funcionalidades não desenvolvidas (para cumprir o requisito)
@app.route('/disciplinas')
@app.route('/alunos')
@app.route('/cursos')
@app.route('/ocorrencias')
def unavailable():
    return render_template('unavailable.html', current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Criar o banco de dados se não existir (Executa uma vez ao iniciar)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)