from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class CpfForm(FlaskForm):
    cpf = StringField("Informe os 9 primeiros dígitos do seu CPF", validators=[InputRequired(message="Esse campo é obrigatório")])
    submit = SubmitField("Calcular")
    reset = SubmitField("Calcular Novamente")