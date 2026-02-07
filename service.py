from models import MLModel

class Preprocessor:
    def transform(self, X):
        return X
    
class ModelNotTrainedError(Exception):
    pass
    
class ModelService:
    def __init__(self, model: MLModel, preprocessor: Preprocessor):
        self.model = model               # Composition
        self.preprocessor = preprocessor  # Inject
        self.__trained = False

    def train(self, X, y):
        Xp = self.preprocessor.transform(X)
        self.model.fit(Xp, y)
        self._trained = True


    def infer(self, X):
        if self.__trained == False:
            raise ModelNotTrainedError("Before train")
        else:
            Xp = self.preprocessor.transform(X)
            return self.model.predict(Xp)
    
    


# Composition.It is composition, because ("model=self.model. >>model:Model") the connection is composition.
# The connection not Inheritance.Inheritance is hard connection.The connection is soft.ModelService has-a MLModel

    def print_model_name(self):
        print(f"Model: {self.model.name}")



