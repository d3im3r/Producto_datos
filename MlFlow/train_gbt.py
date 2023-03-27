
#Librerías
import pandas as pd
import numpy as np
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.metrics import  classification_report, accuracy_score, roc_auc_score
import os
import sys
import warnings
warnings.filterwarnings("ignore")
from utils import Utils
utils = Utils()

def run():
    #
    # Entrena un modelo sklearn Gradient Boosting Trees...
    #
    # Cargando datos...

    # Cargando datos...
    path = os.path.dirname(__file__)
    filename = os.path.join(path, 'processed_data_.csv')
    data=utils.load_data(path=filename)
    data = data.dropna()

    # Partiendo variable dependientes e independientes...
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
    
    # Particionamiento entrenamiento y validación...
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)

    # Definiendo hiperparámetros...
    learning_rate = float(sys.argv[1])
    n_estimators = int(sys.argv[2])
    max_depht = int(sys.argv[3])
    verbose = int(sys.argv[4])


    print('Tracking directory:', mlflow.get_tracking_uri())

    with mlflow.start_run():

        estimator = GradientBoostingClassifier(learning_rate=learning_rate, n_estimators=n_estimators, max_depth=max_depht)
        estimator.fit(X_train, y_train)
        accuracy, recall, roc_score = utils.eval_metrics(y_test, y_pred=estimator.predict(X_test))
        if verbose > 0:
            utils.report(estimator, accuracy, recall, roc_score)

            mlflow.log_param("learning_rate", learning_rate)
            mlflow.log_param("n_estimators", n_estimators)
            mlflow.log_param("max_depth", max_depht)

            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("roc_score", roc_score)

            mlflow.sklearn.log_model(estimator, "model")

<<<<<<< HEAD
        # -------------------------------------------------------------------------------
        # evaluación del modelo
        #
        eval_data = X_test
        eval_data['target'] = y_test

        # mlflow.sklearn.log_model(estimator, "model")
        model_info = mlflow.sklearn.log_model(estimator, "model")
        mlflow.evaluate(
            model_info.model_uri,
            eval_data,
            targets="target",
            model_type="classifier" # "regressor" | "classifier"
        )
=======
            # client = mlflow.MlflowClient()
            # client.create_model_version(
            #     name=f"sklearn-{learning_rate}-learning_rate-{n_estimators}-n_estimators-{max_depht}-max_depht",
            #     source=f"mlruns/0/{mlflow.start_run().info.run_id}/artifacts/model"
            #     run_id=mlflow.start_run().info.run_id,
            # )
>>>>>>> 62a412faa46d94c10a7a6873f05465591c0abae2


if __name__ == "__main__":
    run()
