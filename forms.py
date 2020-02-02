from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginUsuario(FlaskForm):
    name = StringField('Nombre',validators=[DataRequired(), Length(max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')