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
json_path = os.path.join(module_path, "./static/json/data.json")
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
            canceled_percent = round(canceled_percent,5)
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
    json_text = open(json_path)

    json_file = json.load(json_text)
    string = json_file["data"]
    accuracy = json_file["accuracy"]
    # string = ""
    # with open(json_path) as json_bytes:
    #     string = json_bytes.read().replace('"', '')
    
    # To read a JSON File
    lines = string.split('\n')
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    _ = lines[0].split()
    values = [line.split() for line in lines[1:]]

    precision_non_canceled = values[0][1]
    precision_canceled = values[1][1]
    precision_macro_avg = values[3][2]
    precision_weithted_avg = values[4][2]
    recall_non_canceled = values[0][2]
    recall_canceled = values[1][2]
    recall_macro_avg = values[3][3]
    recall_weighted_avg = values[4][3]
    f1_score_non_canceled = values[0][3]
    f1_score_canceled = values[1][3]
    f1_score_accuracy = values[2][1]
    f1_score_macro_avg = values[3][4]
    f1_score_weighted_avg = values[4][4]
    support_non_canceled = values[0][4]
    support_canceled = values[1][4]
    support_accuracy = values[2][2]
    support_macro_avg = values[3][5]
    support_weighted_avg = values[4][5]
    

    context = {
        'precision_non_canceled': precision_non_canceled,
        'precision_canceled': precision_canceled,
        'precision_macro_avg': precision_macro_avg,
        'precision_weithted_avg': precision_weithted_avg,
        'recall_non_canceled': recall_non_canceled,
        'recall_canceled': recall_canceled,
        'recall_macro_avg': recall_macro_avg,
        'recall_weighted_avg': recall_weighted_avg,
        'f1_score_non_canceled': f1_score_non_canceled,
        'f1_score_canceled': f1_score_canceled,
        'f1_score_accuracy': f1_score_accuracy,
        'f1_score_macro_avg': f1_score_macro_avg,
        'f1_score_weighted_avg': f1_score_weighted_avg,
        'support_non_canceled': support_non_canceled,
        'support_canceled': support_canceled,
        'support_accuracy': support_accuracy,
        'support_macro_avg': support_macro_avg,
        'support_weighted_avg': support_weighted_avg,
        'accuracy': round(accuracy*100, 2)
        }
    return render_template("metrics.html", **context)



if __name__ == '__main__':
    #model = joblib.load("./models/best_model.pkl")
    app.run(port=8080, debug=True)