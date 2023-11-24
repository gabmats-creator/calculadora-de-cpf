from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, IntegerField, DateField, PasswordField, SelectField
from wtforms.validators import InputRequired, NumberRange, Email, Length, EqualTo

class CpfForm(FlaskForm):
    cpf = StringField("Informe o CPF", validators=[InputRequired(message="Esse campo é obrigatório")])
    submit = SubmitField("Calcular")
    reset = SubmitField("Calcular Novamente")