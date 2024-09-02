class Car:
    total_car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand+'!'

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are a good way to get around"
   
    def model(self):
        return self.__model


class ElecticCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size


    def fuel_type(self):
        return "Electric charge"
    

class Battery:
    def battery_info(self):
        return "This is a battery"

class Engine:
    def engine_info(self):
        return "This is an engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass
    

mycar=Car("Toyota","Corolla")

print(mycar.full_name())

my_new_car=Car("Tata","Safari")


mytesla=ElecticCar("Tesla","Model S","85kWh")
print(mytesla.full_name())

print(mytesla.get_brand())

safari=Car("Tata","Safari")
safari.model="Nexon"

print(safari.model)

print(mytesla.fuel_type())

test=Car("test","test")
print(test.total_car)
print(Car.total_car)
print(safari.total_car)
print(Car.general_description())

print(isinstance(mytesla,Car)) #returns false
print(isinstance(mytesla,ElecticCar)) # returns true


my_new_tesla=ElectricCarTwo("Tesla","Model S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info()) 


