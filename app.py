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
        pesos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cpf = list(cpf_base)
        for i in range(len(pesos)):
            print(pesos[i], cpf[i])
            soma += pesos[i] * int(cpf[i])

        resto = soma % 11
        primeiro_digito = resto if resto < 10 else 0

        # Adiciona o primeiro dígito verificador ao CPF base
        cpf.append(str(primeiro_digito))
        # Calcula o segundo dígito verificador
        soma = 0
        pesos.insert(0, 0)
        for i in range(len(pesos)):
            print(pesos[i], cpf[i])
            soma += pesos[i] * int(cpf[i])

        resto = soma % 11
        segundo_digito = resto if resto < 10 else 0

        # Adiciona o segundo dígito verificador ao CPF completo
        cpf.append(str(segundo_digito))
        return ''.join(cpf)

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
