### Aqui inicia el desarrollo de la aplicacion...
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap
import flask
import plotly
import plotly.express as px
import json
import os


module_path = os.path.dirname(__file__)
folder_path = os.path.join(module_path, "models/gbt_model.pkl")
#folder_path = os.path.join(module_path, "../Data/Preprocessing")

app = Flask(__name__)
# Implementando Bootstrap...
bootstrap = Bootstrap(app)

# Manejo de errores con html personalizado...
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

# Definiendo ruta para correr...
@app.route('/')
def index():
    # user_ip = request.cookies.get('user_ip')
    # context = {
    #     'user_ip':user_ip,
    #     'todos': todos
    # }
    return render_template('inicio.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 5)
    #/home/d3im3r/Dropbox/Maestría/Productos_Datos/Producto_datos/App/models/gbt_model.pkl
    loaded_model = joblib.load(folder_path)
    result = loaded_model.predict_proba(to_predict)
    return result[:,1]

# Definiendo ruta para correr...
@app.route('/result',methods = ['POST'])

def result():
       if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        try:
            to_predict_list = list(map(float, to_predict_list))
            result = ValuePredictor(to_predict_list)
            canceled_percent = float(result[0])*100
            canceled_percent = round(canceled_percent,2)
            if float(result)>=0.5:
                prediction= 'El cliente muy probablemente CANCELARÁ'
            elif float(result)<0.5:
                prediction= 'El cliente muy probablemente NO CANCELARÁ'
            else:
                prediction=f'{int(result)} No-definida'
        except ValueError:
            prediction='Error en el formato de los datos'
        context = {
        'prediction':prediction,
        'canceled_percent': canceled_percent
        }

        return render_template("result.html", **context)


@app.route('/metrics')
def metrics():
    return render_template("metrics.html")



if __name__ == '__main__':
    #model = joblib.load("./models/best_model.pkl")
    app.run(port=8080, debug=True)