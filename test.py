# from dataclasses import dataclass

# @dataclass
# class Person:
#     name:str
#     age:int



# class Person2:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(People):
#     def __init__(self, name, age, passport):
#        super().__init__(name, age)
#        self.passport = passport

#     def __str__(self):
#         return f"{self.name}. {self.age}. {self.passport}"


# student1 = Student("Alimurod",22,"Ad899898")

# print(student1.__str__())


# class Student1:

#     def __init__(self, name, age, passport):
#         self.people = People(name, age)
#         self.passport = passport

#     def __str__(self):
#         return f"{self.people.name}. {self.people.age}. {self.passport}"
    

# student2 = Student("Jamshidbek",22,"Ad899898")

# print(student2.__str__())


# from abc import ABC,abstractmethod

# class PaymentStrategy(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass  


# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(People):
#     def __init__(self, name, age, passport):
#        super().__init__(name, age)
#        self.passport = passport
    
#     @property
#     def universitet_name(self):
#         return f"TATU{self.summa(3,4)}"
    
#     @classmethod
#     def class_name(cls):
#         return f"People"
    
#     @staticmethod

#     def summa(x,y):
#         return x + y


#     def __str__(self):
#         return f"{self.name}. {self.age}. {self.passport}"
    


# student3 = Student("Jamshidbek",22,"Ad899898")

# print(student3.universitet_name)
# print(Student.class_name())

# print(student3.class_name())