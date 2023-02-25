# Predicción de las cancelaciones de reservas en los hoteles, a partir de los datos 
import os
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', 10)


#####################################################################################################################################


def main_work():
    data_raw = load_data()
    data_selected = select_data(data_raw)
    data_4_use = define_status(data_selected,flag=21)
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


def define_status(booking,flag=7):
    data = booking.apply(lambda row: categorize_status(row,flag), axis=1)
    booking.insert(loc=3,
                   column='status',
                   value = data)
    return booking

def categorize_status(row,flag=7):
    if row['lead_time'] == 0:
        return 'closed'
    elif row['lead_time'] > 0 and row['lead_time'] <= flag:
        return 'in_progress'
    else:
        return 'open'


datos=main_work()
datos=data_clean_columns(datos,"agent","company")

print(datos.head())
