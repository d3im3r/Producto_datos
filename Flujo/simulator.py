# Predicción de las cancelaciones de reservas en los hoteles, a partir de los datos 
import os
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# pd.set_option('display.max_columns', 10)


#####################################################################################################################################
path_ = os.path.dirname(__file__)
categories_unusefull = ["agent","company",'days_in_waiting_list', 'arrival_date_year', "arrival_date_month",'assigned_room_type', 'booking_changes',
                        'reservation_status', 'country', 'days_in_waiting_list']

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
    data_status = define_status(data_datetime_corrected)
    data_feeder = data_filter(data_status)
    data_OHE = one_hot_encoding(data_feeder)
    print(" One-Hot-Encoding... ".center(80,"*"), data_OHE.shape, sep="\n")
    data_4_use = data_scaling(data_OHE)
    print(" Escalando data... ".center(80,"*"), data_4_use.shape,data_4_use.head(),sep="\n")
    data_4_use.to_csv(f"../Data/Preprocessing/preprocessing_data_{1}.csv", index = False, header = True)
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
    #print("#"*50,"\nDimension del dataframe: ",booking.shape)
    #print("#"*50,"\nNumero de registros por hotel: \n",booking.hotel.value_counts())
    #print("#"*50,"\nDatos nulos presentes",booking.isnull().sum())
    return booking

## limpieza de datos
def data_clean_columns(booking,heads_to_remove=[]):
    # Eliminando variables que no aportaran al modelo...
    for head in heads_to_remove:
        if head in booking[0:]:
            booking.drop(head, axis=1, inplace=True)
    #print("#"*50,"\nDatos nulos presentes después de la limpieza",booking.isnull().sum())
    return booking



def define_status(booking,flag=21):
    data = booking.apply(lambda row: categorize_status(row,flag), axis=1)
    booking.insert(loc=3,
                   column='status',
                   value = data)
    
    return booking

def categorize_status(row,flag=21):
    if row['lead_time'] == 0:
        return 'closed'
    elif row['lead_time'] > 0 and row['lead_time'] <= flag:
        return 'in_progress'
    else:
        return 'open'

def data_filter(booking):
    booking = booking[booking["lead_time"]<=21]
    return booking


def datetime_adjust(booking):
    booking['reservation_status_date'] = pd.to_datetime(booking['reservation_status_date'])
    booking['year_res_status_date'] = booking['reservation_status_date'].dt.year
    booking['month_res_status_date'] = booking['reservation_status_date'].dt.month
    booking['day_res_status_date'] = booking['reservation_status_date'].dt.day
    # Eliminando reservation status date y arrival month...
    booking.drop(['reservation_status_date'] , axis = 1, inplace = True)
    return booking

def one_hot_encoding(booking):
    return pd.get_dummies(booking)

def data_scaling(booking):
    # Escalando...
    scaler = MinMaxScaler()
    booking_processing_scaled = scaler.fit_transform(booking)
    # Convertir a tipo DataFrame...
    data_processing_scaled = pd.DataFrame(booking_processing_scaled)
    # Obteniendo nombres columnas...
    data_processing_scaled.columns = booking.columns
    data_processing_scaled.head()
    #print(data_processing_scaled.shape)
    return data_processing_scaled


##########################