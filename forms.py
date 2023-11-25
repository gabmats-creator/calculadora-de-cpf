from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class CpfForm(FlaskForm):
    cpf = StringField("Informe o CPF", validators=[InputRequired(message="Esse campo é obrigatório")])
    submit = SubmitField("Calcular")
    reset = SubmitField("Calcular Novamente")