# Predicción de las cancelaciones de reservas en los hoteles, a partir de los datos 
import os
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas
import folium
import geopandas
import folium
import plotly.io as pli
from sklearn.preprocessing import MinMaxScaler

# Don´t show warnings......
import warnings

warnings.filterwarnings("ignore")


#####################################################################################################################################


def main_work():
    data_raw = load_data()
    data_4_use = select_data(data_raw)
    return data_4_use


## carga de datos
def load_data():
    path_ = os.path.dirname(__file__)
    filename = os.path.join(path_, "hotel_bookings.csv")
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found")
    booking = pd.read_csv(filename, sep=",")
    return booking

## muestreo aleatorio simple
def select_data(booking,instances=10000,seed=42):
    booking = booking.sample(n=instances, random_state=seed)
    print("#"*50,"\nDimension del dataframe: ",booking.shape)
    print("#"*50,"\nNumero de registros por hotel: \n",booking.hotel.value_counts())
    print("#"*50,"\nDatos nulos presentes",booking.isnull().sum())
    return booking

## limpieza de datos
def data_clean_columns(booking,head1=None,head2=None,head3=None,head4=None,head5=None):
    # Eliminando variables que no aportaran al modelo...
    if head1 in booking[0:]:
        booking.drop(head1, axis=1, inplace=True)
    if head2 in booking[0:]:
        booking.drop(head2, axis=1, inplace=True)
    if head3 in booking[0:]:
        booking.drop(head3, axis=1, inplace=True)
    if head4 in booking[0:]:
        booking.drop(head4, axis=1, inplace=True)
    if head5 in booking[0:]:
        booking.drop(head5, axis=1, inplace=True)
    booking = booking.dropna()
    print("#"*50,"\nDatos nulos presentes después de la limpieza",booking.isnull().sum())
    return booking


datos=main_work()
datos=data_clean_columns(datos,"agent","company")

print(datos.head())
