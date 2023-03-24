import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score, ConfusionMatrixDisplay, classification_report
import os

module_path = os.path.dirname(__file__)
folder_path = os.path.join(module_path, "models/gbt_model.pkl")

class Utils:
    # Funcion para carga de datos...
    def load_data(self, path):
        return pd.read_csv(path)
    
    

    # Funcion para separar covariables y variable respuesta...
    def features_target(self, dataset, drop_cols, y):
        X = dataset.drop(drop_cols,axis=1)
        y = dataset[y]
        return X,y
    

    # Particion de datos en entrenamiento y validacion...
    def make_train_test_split(x, y, testSize = 0.20, randomState=42):
        (x_train, x_test, y_train, y_test) = train_test_split(
            x,
            y,
            test_size=testSize,
            random_state=randomState)
        return x_train, x_test, y_train, y_test

    
    # Metricas de evaluacion del modelo...
    def eval_metrics(y_true, y_pred):
        accuracy = accuracy_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        roc_score = roc_auc_score(y_true, y_pred)

        return accuracy, recall, roc_score
    

    # Reporte de metricas...
    def report(estimator, accuracy, recall, roc_score):
        print(estimator, ":", sep="")
        print(f"  Accuracy: {accuracy}")
        print(f"  Recall: {recall}")
        print(f"  ROC Score: {roc_score}")



    def model_export(self,clf,score):
        print(score)
        joblib.dump(clf,folder_path)

    # Coment...
