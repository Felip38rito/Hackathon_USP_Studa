from flask import Flask
from flask import render_template
from flask import request

import pandas as pd

from studa import Agrupamento

# from wtforms import StringField, PasswordField

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("signin.twig")


@app.route("/complete", methods=['GET', 'POST'])
def complete():
    # print( request.values.get('nome') )
    return render_template("complete.twig", name=request.values.get("nome"))


@app.route("/results", methods=['GET', 'POST'])
def results():
    req = request.values
    
    data = pd.DataFrame(
        [
            ['NOME', 'FACULDADE', 'CURSO', 'SEMESTRE', 'IDADE', 'LINGUA', 'INTERCAMBIO', 'INICIACAO CIENTIFICA', 'EXPERIENCIA_PROFISSIONAL_MESES', 'FORMACAO'],
            [req.get('inputNome'),
            req.get('inputFaculdade'), 
            req.get('inputCurso'), 
            req.get('inputSemestre'), 
            req.get('inputIdade'), 
            req.get('inputLinguas'), 
            req.get('inputIntercambio'), 
            req.get('inputIC'), 
            req.get('inputExperiencia'), 
            req.get('inputGraduacao')]
        ]
    )

    cluster = pd.read_csv("cluster.csv", sep=";")
    # print(cluster)
    stu = Agrupamento(pd.read_csv('BASE_FULL.csv', sep=";"), cluster, req.get('inputCurso'))

    # vamos calcular o cluster com os resultados
    # print(data)
    # print(stu)
    # print(cluster)

    cluster = cluster.loc[(cluster['CLUSTER'] == stu)]
    cluster = cluster.loc[(cluster['curso'] == req.get('inputCurso'))]
    # print(cluster)
    cluster['ESTRELAS'] = cluster['ESTRELAS']*1


    return render_template("results.twig", val=request.values, cluster=pd.np.asarray(cluster))
    
