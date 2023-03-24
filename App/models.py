import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

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
    def grid_training(self,X,y):

        best_score = 999
        best_model = None

        for name, reg in self.reg.items():

            grid_reg = RandomizedSearchCV(reg,self.params[name],cv=3).fit(X,y.values.ravel())
            score = np.abs(grid_reg.best_score_)

            if score < best_score:
                best_score = score
                best_model = grid_reg.best_estimator_


        utils = Utils()
        utils.model_export(best_model,best_score)