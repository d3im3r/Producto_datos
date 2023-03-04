from utils import Utils
from models import Models

if __name__ == "__main__":
    
    utils = Utils()
    models = Models()

    data = utils.load_data("../Data/Preprocessing/preprocessing_data.csv")
    # Partir dataset:
    X,y = utils.features_target(data,[data.drop("is_canceled",axis=1)],
        ["is_canceled"])
    
    # Training...
    models.grid_training(X,y)

    print(data)
