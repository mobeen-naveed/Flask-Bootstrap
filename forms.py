from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class ContactForm(FlaskForm):
    contact_name = StringField('Name', validators=[DataRequired()])
    contact_email = StringField('Email',
                        validators=[DataRequired(), Email()])
    contact_message = TextAreaField('Message', validators=[DataRequired()])                    
    submit = SubmitField('Submit')  