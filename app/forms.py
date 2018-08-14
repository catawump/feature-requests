from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from wtforms.fields.html5 import DateField, IntegerField
from app.models import User

# Login Form

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# New User Registraion Form

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# Feature Request Form

class RequestForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(min=1, max=140)])
    description = TextAreaField('Description:', validators=[DataRequired(), Length(min=1, max=140)])
    client = SelectField('Client:', choices=[('Client A', 'Client A'), ('Client B', 'Client B'), ('Client C', 'Client C')], coerce=unicode, option_widget=None, validators=[DataRequired()])
    client_priority = IntegerField('Client Priority:', validators=[DataRequired(), NumberRange(min=1, max=None)])
    product_area = SelectField('Product Area:', choices=[('Policies', 'Policies'), ('Billing', 'Billing'), ('Claims', 'Claims'), ('Reports', 'Reports')], coerce=unicode, option_widget=None, validators=[DataRequired()])
    target_date = DateField('Target Date:', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')