""" Necessary imports """
from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Regulation, Regulation_Types
from app.forms import EditRuleForm

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

@app.route('/edit_rule/<int:id>', methods=['GET', 'POST'])
def edit_rule(id):
    form = EditRuleForm()
    if form.validate_on_submit():
        rule = Regulation()
        rule.Regulation_ID = form.id.data
        rule.Regulation_Reference = form.reference.data
        rule.Regulation_Start_Date = form.start_date.data
        rule.Regulation_End_Date = form.end_date.data
        rule.Regulation_Number = form.number.data
        rule.Regulation_Parent = form.parent.data
        rule.Regulation_Text = form.text.data
        rule.Regulation_Comment = form.comment.data
        # Save to DB
        flash('Changes have been saved.')
        return redirect(url_for('viewrules'))
    elif request.method == 'GET':
        rule = Regulation.query.filter(Regulation.Regulation_ID==id).first() #query db
        form.id.data = rule.Regulation_ID
        form.reference.data = rule.Regulation_Reference
        form.start_date.data = rule.Regulation_Start_Date
        form.end_date.data = rule.Regulation_End_Date
        form.number.data = rule.Regulation_Number
        form.parent.data = rule.Regulation_Parent
        form.text.data = rule.Regulation_Text
        form.comment.data = rule.Regulation_Comment
    return render_template('edit_rule.html', form=form)