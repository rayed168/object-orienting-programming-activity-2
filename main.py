class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
Mercedes=Vehicle(200,70)
Lexus=Vehicle(180,65)
print("I am mercedes. my max speed is",Mercedes.max_speed)
print(Mercedes.mileage)
print("I am lexus. my max speed is",Lexus.max_speed)
print(Lexus.mileage)