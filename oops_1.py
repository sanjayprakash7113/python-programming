class Test:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")

obj = Test()


class Demo:
    def __del__(self):
        print("Object is being deleted")

d = Demo()
del d  # explicitly deleting object


class Car:
    def __init__(self, model, color):
        self.model = model  # instance attribute
        self.color = color

# Create object
my_car = Car("red", "bmw")

print(my_car.model)  # BMW
print(my_car.color)  # Red
