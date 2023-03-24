import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, accuracy_score

from utils import Utils


class Models:

    def __init__(self):
        self.reg = {
            "LogisticRegression": LogisticRegression(random_state=42),
            "GradientBoostingClassifier": GradientBoostingClassifier(random_state=42)
        }

        self.params ={
            "LogisticRegression": {
                "penalty": ['l1', 'l2'],
                "C": [0.4,1.0,1.5],
                "solver": ["liblinear"]
            }, "GradientBoostingClassifier": {
                "loss": ["los_loss","exponential"],
                "learning_rate": [0.001, 0.01, 0.1, 0.2],
                "n_estimators": [100, 200, 300, 400],
                "max_depth": [3, 5, 8, 10]
            }
        }
    
    # Definir funcion de ejecucion codigo...
    def grid_training(self,x_train,y_train,x_test,y_test):

        best_score = 999
        best_model = None

        for name, reg in self.reg.items():

            grid_reg = RandomizedSearchCV(reg,self.params[name],cv=3).fit(x_train,y_train.values.ravel())
            score = np.abs(grid_reg.best_score_)

            if score < best_score:
                best_score = score
                best_model = grid_reg.best_estimator_

            gbt_preds_opt = grid_reg.predict(x_test)
            accuracy = accuracy_score(y_test,gbt_preds_opt)

            target_names = ['Non-Canceled', 'Canceled']
            classification_repo = classification_report(y_test, gbt_preds_opt, target_names=target_names)


        utils = Utils()
        utils.model_export(best_model,best_score)
        return classification_repo, accuracy