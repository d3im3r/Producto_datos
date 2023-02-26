# Predicción de las cancelaciones de reservas en los hoteles, a partir de los datos 
import os
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# pd.set_option('display.max_columns',51)


#####################################################################################################################################
categories_unusefull = ["agent","company",'days_in_waiting_list', 'arrival_date_year', "arrival_date_month",'assigned_room_type', 'booking_changes',
                        'country', 'days_in_waiting_list']
data_path = "hotel_bookings.csv"
flag = 21 # Cantidad de dias con los que se van a analizar

def main_work():
    data_raw = load_data()
    print(" Dimensionalidad datos originales... ".center(80,"*"))
    print(data_raw.shape)
    data_selected = select_data(data_raw)
    print(" Muestreando data... ".center(80,"*"), data_selected.shape, data_selected.head(), sep="\n")
    data_clean = data_clean_columns(data_selected,categories_unusefull)
    print(" Limpiando data... ".center(80,"*"),data_clean.head(), sep="\n")
    data_datetime_corrected = datetime_adjust(data_clean)
    print(" Definiendo variable status... ".center(80,"*"))
    data_status = define_status(data_datetime_corrected,flag)
    print(data_status.loc[:, ['reservation_status', "is_canceled"]])
    data_feeder = data_filter(data_status,flag)
    data_OHE = one_hot_encoding(data_feeder)
    print(" One-Hot-Encoding... ".center(80,"*"), data_OHE.shape, sep="\n")
    data_4_use = data_scaling(data_OHE)
    print(" Escalando data... ".center(80,"*"), data_4_use.shape,data_4_use.head(),sep="\n")
    data_4_use.to_csv(f"../Data/Preprocessing/preprocessing_data_{1}.csv", index = False, header = True)
    return data_4_use

'''
Carga de informacion
Lectura de archivo csv en la ruta data_path
'''
def load_data():
    path_ = os.path.dirname(__file__)
    filename = os.path.join(path_, data_path)
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found")
    dataframe = pd.read_csv(filename, sep=",")
    return dataframe

'''
Muestreo aleatorio simple
'''
def select_data(dataframe,instances=10000,seed=42):
    dataframe = dataframe.sample(n=instances, random_state=seed)
    return dataframe

'''
Se limpian datos de columnas poco relevantes para el 
modelo final
'''
def data_clean_columns(dataframe,heads_to_remove=[]):
    for head in heads_to_remove:
        if head in dataframe[0:]:
            dataframe.drop(head, axis=1, inplace=True)
    return dataframe

'''
Se cambia el estado de reserva en base a si fue cancelada 
o no en el tiempo que hay entre la reserva y el dia 
de llegada al hotel
'''
def define_status(dataframe,flag=21):
    dataframe["reservation_status"] = dataframe.apply(lambda row: categorize_status(row,flag), axis=1)
    return dataframe

def categorize_status(dataframe,flag=21):
    if dataframe['is_canceled'] == 1:
        result = "canceled"
    else:
        if dataframe['lead_time'] == 0:
            result = "closed"
        elif dataframe['lead_time'] > 0 and dataframe['lead_time'] <= flag:
            result = "in_progress"
        else:
            result = "open"
    return result

'''
Se seleccionan los datos que se encuentren dentro de 
'''
def data_filter(dataframe,flag=21):
    dataframe = dataframe[dataframe["lead_time"]<=flag]
    return dataframe

'''
Se convierte la fecha de reservation status a año, mes y dia
'''
def datetime_adjust(dataframe):
    dataframe['reservation_status_date'] = pd.to_datetime(dataframe['reservation_status_date'])
    dataframe['year_res_status_date'] = dataframe['reservation_status_date'].dt.year
    dataframe['month_res_status_date'] = dataframe['reservation_status_date'].dt.month
    dataframe['day_res_status_date'] = dataframe['reservation_status_date'].dt.day
    # Eliminando reservation status date y arrival month...
    dataframe.drop(['reservation_status_date'] , axis = 1, inplace = True)
    return dataframe

'''
Se convierten todos los valores a numeros entre 0 y 1
'''
def one_hot_encoding(dataframe):
    return pd.get_dummies(dataframe)

'''
Se escalan los datos mediante fit_transform
'''
def data_scaling(dataframe):
    # Escalando...
    scaler = MinMaxScaler()
    dataframe_processing_scaled = scaler.fit_transform(dataframe)
    # Convertir a tipo DataFrame...
    data_processing_scaled = pd.DataFrame(dataframe_processing_scaled)
    # Obteniendo nombres columnas...
    data_processing_scaled.columns = dataframe.columns
    data_processing_scaled.head()
    return data_processing_scaled


##########################