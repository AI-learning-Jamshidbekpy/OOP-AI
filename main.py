# from models import SklearnModel, TorchModel
# from service import ModelService


# model1 = SklearnModel()
# model2 = TorchModel()

# service1 = ModelService(model1)
# service2 = ModelService(model2)


# service1.train(10,5)
# print(service1.infer(10))

# service2.train(6,8)
# print(service2.infer(6))


# # If I change model, of course change response ModelService.Because, ModelService's response soft connected MlModel


# service1.print_model_name()
# service2.print_model_name()

from models import SklearnModel, TorchModel
from service import ModelService


model1 = SklearnModel()
model2 = TorchModel()

service1 = ModelService(model1, "preprocessor1")
service2 = ModelService(model2, "preprocessor2")


service1.train(10,5)
print(service1.infer(10))

service2.train(6,8)
print(service2.infer(6))


# If I change model, of course change response ModelService.Because, ModelService's response soft connected MlModel


service1.print_model_name()
service2.print_model_name()


service3 = ModelService(model1, "preprocessor3")


print(service3.infer(10))
service3.train(10,5)


print(TorchModel.normalize([10, 10, 10]))