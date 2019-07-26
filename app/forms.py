from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class EditRuleForm(FlaskForm):
    id = StringField('Regulation ID', validators=[DataRequired()])
    reference = StringField('Standard', validators=[DataRequired()])
    start_date = DateField('Start Date')
    end_date = DateField('End Date')
    number = StringField('Number', validators=[DataRequired()])
    parent = StringField('Parent Rule')
    text = TextAreaField('Rule Text', validators=[DataRequired()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')