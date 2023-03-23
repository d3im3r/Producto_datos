# Archivo para flujo de Machine Learning...
from utils import Utils
from models import Models
from sklearn.model_selection import train_test_split
if __name__ == "__main__":
    
    utils = Utils()
    models = Models()

    data = utils.load_data("../Data/Preprocessing/processed_data_.csv")
    data = data.dropna()
    # Partir dataset:
    X,y = utils.features_target(data, ["is_canceled"], ["is_canceled"])
    # Particion datos entrenamiento y validacion...
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)
    # Training...
    models.grid_training(X_train,y_train)

    print(data)
