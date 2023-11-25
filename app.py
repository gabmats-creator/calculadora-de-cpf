from flask import (
    Flask,
    render_template,
    request,
)
from forms import CpfForm
import os
import re


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFz"
    )

    def calcular_digitos_verificadores(cpf_base):
        # Calcula o primeiro dígito verificador
        soma = 0
        peso = 10
        for digito in cpf_base:
            soma += int(digito) * peso
            peso -= 1

        resto = soma % 11
        primeiro_digito = 0 if resto < 2 else 11 - resto

        # Adiciona o primeiro dígito verificador ao CPF base
        cpf_base += str(primeiro_digito)

        # Calcula o segundo dígito verificador
        soma = 0
        peso = 11
        for digito in cpf_base:
            soma += int(digito) * peso
            peso -= 1

        resto = soma % 11
        segundo_digito = 0 if resto < 2 else 11 - resto

        # Adiciona o segundo dígito verificador ao CPF completo
        cpf_completo = cpf_base + str(segundo_digito)

        return cpf_completo

    @app.route("/", methods=["GET", "POST"])
    def index():
        cpf = None
        erro = None
        form = CpfForm()
        if request.form.get("Recalcular"):
            return render_template(
                "index.html", title="Calculadora de CPF", cpf=None, form=form
            )
        if form.validate_on_submit():
            if len(form.cpf.data) == 9:
                cpf = calcular_digitos_verificadores(form.cpf.data)
                cpf = re.sub(r'(.{3})(.{3})(.{3})', r'\1.\2.\3-', cpf)
        return render_template(
            "index.html", title="Calculadora de CPF", cpf=cpf, form=form, erro=erro
        )

    return app
