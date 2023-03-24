# Archivo para flujo de Machine Learning...
from utils import Utils
from models import Models
from sklearn.model_selection import train_test_split
import os

if __name__ == "__main__":
    
    utils = Utils()
    models = Models()

    module_path = os.path.dirname(__file__)
    folder_path = os.path.join(module_path, "../Data/Preprocessing/processed_data_.csv")
    
    data = utils.load_data(folder_path)
    data = data.dropna()
    # Partir dataset:
    X,y = utils.features_target(data, ['is_canceled', 'lead_time', 'arrival_date_week_number',
       'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children',
       'babies', 
       'previous_bookings_not_canceled','year_res_status_date',
       'month_res_status_date', 'day_res_status_date', 'hotel_City Hotel',
       'hotel_Resort Hotel', 'meal_BB', 'meal_FB', 'meal_HB', 'meal_SC',
       'meal_Undefined', 'market_segment_Aviation',
       'market_segment_Complementary', 'market_segment_Corporate',
       'market_segment_Direct', 'market_segment_Groups',
       'market_segment_Offline TA/TO', 'market_segment_Online TA',
       'market_segment_Undefined', 'distribution_channel_Corporate',
       'distribution_channel_Direct', 'distribution_channel_GDS',
       'distribution_channel_TA/TO', 'distribution_channel_Undefined',
       'reserved_room_type_A', 'reserved_room_type_B', 'reserved_room_type_C',
       'reserved_room_type_D', 'reserved_room_type_E', 'reserved_room_type_F',
       'reserved_room_type_G', 'reserved_room_type_H', 'reserved_room_type_L',
       'reserved_room_type_P', 'deposit_type_No Deposit',
       'deposit_type_Non Refund', 'deposit_type_Refundable',
       'customer_type_Contract', 'customer_type_Group',
       'customer_type_Transient', 'customer_type_Transient-Party',
       'reservation_status_processed'], ["is_canceled"])
    # Particion datos entrenamiento y validacion...
    print('Iniciando entrenameinto del modelo....')
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)
    models.grid_training(X_train,y_train)
    print('Entrenamiento del modelo finalizado....')
    print('*'*100)
    print(data)
