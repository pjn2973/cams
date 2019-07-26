""" Necessary imports """
from flask import render_template
from app import app, db
from app.models import Regulation, Regulation_Types

@app.route('/')
@app.route('/index')
def index():
    """ temp """
    user = {'username':'Peter'}
    return render_template('index.html', user=user)

@app.route('/viewrules')
def viewrules():
    """ Return rules """
    regulations = Regulation.query.order_by(Regulation.Regulation_Number).all()
    
    return render_template('rules.html', user={'username':'Peter'}, regulation=regulations)