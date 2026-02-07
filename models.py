from abc import ABC, abstractmethod
class MLModel(ABC):

    @abstractmethod
    def fit(self, X, y) -> None:
        pass
    
    @abstractmethod
    def predict(self, X) -> list:
        pass

    @property
    def name(self):
        return f"{self.__class__.__name__.lower()}_dummy"


# m = MLModel() 
# TypeError: Can't instantiate abstract class MLModel without an implementation for abstract methods 'fit', 'predict'


class SklearnModel(MLModel):

    def __init__(self):
        self.is_fitted = False

    def fit(self, X, y) ->None:
        self.is_fitted = True
        return self.is_fitted

    def predict(self, X) -> list:
        if self.is_fitted:
            return [1] * X
        raise RuntimeError("Model fit qilinmagan")

    
    @classmethod
    def from_config(cls, config: dict):
        cls.config = {"Model":SklearnModel}
        return cls.config


class TorchModel(MLModel):

    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def fit(self, X, y) ->None:
        pass

    def predict(self, X) -> list:
        return 1 if X > self.threshold else 0
    
    @staticmethod
    def normalize(X):
        min_x = min(X)
        max_x = max(X)

        if min_x == max_x:
            return X  

        return [(x - min_x) / (max_x - min_x) for x in X]
    
    

class RuleBasedModel(MLModel):

    def fit(self, X, y) ->None:
        pass

    def predict(self, X) -> list:
        if X % 2 == 0:
            return 1
        elif X % 2 == 1:
            return 0
    

 


    
    



    