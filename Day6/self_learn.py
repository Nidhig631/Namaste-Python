#class and object
# class ==> template 
class Car: #class
    def __init__(self,make,model,year): #method
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0 

    def accelerate(self, increment):
        self.speed = self.speed + increment   


car1 = Car("mahindra","xuv300",2020) #object
print(car1.model)
car2 = Car("mahindra","xuv301",2021)
print(car2.model)
# car1.start()
# car2.start()
a= car1.accelerate(10)
print(a)