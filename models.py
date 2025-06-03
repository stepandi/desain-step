from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    """Formulir untuk login pengguna."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')  # Checkbox untuk "ingat saya"
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    """Formulir untuk registrasi pengguna baru."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

class ResetPasswordRequestForm(FlaskForm):
    """Formulir untuk meminta pengaturan ulang password."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    """Formulir untuk mengatur ulang password pengguna."""
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Reset Password')

class UpdateProfileForm(FlaskForm):
    """Formulir untuk memperbarui profil pengguna (misalnya, email, password)."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password')
    confirm_new_password = PasswordField('Confirm New Password', validators=[
        EqualTo('new_password', message='Passwords must match')])
    submit = SubmitField('Update Profile')
