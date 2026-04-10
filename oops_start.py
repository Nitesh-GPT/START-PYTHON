#Personclass has an function where an automatically initiated methods and function are written ,
#selfMethod are also there to make them accessible in the object instance.

class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def greet (self):
        print(f"my name is {self.name} and i'm {self.age} year old")


Person1 = Person('Nitesh', 20)
Person1.greet()

Person2 = Person('Vivek', 22)
Person2.greet()