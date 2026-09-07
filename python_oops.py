
class Car:
    # 
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  


    def display_info(self):
        return f"This car is a {self.brand} {self.model}."


car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")


print(car1.brand)              
print(car2.display_info())   
