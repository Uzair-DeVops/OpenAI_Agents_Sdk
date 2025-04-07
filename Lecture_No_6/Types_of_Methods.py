# # instance variables
# # class variables or static variables
# # Instance methods 
# # class methods
# # static methods 


# class Human:
#     # class variable
#     specie = "HumanSpecie"
#     # instance variable
#     def __init__(self, name, age):
#         # type: ignore
#         self.name = name
#         self.age = age

#     def myname(self):
#         return "my name is", self.name ,"and age is ", self.age
    
#     # class method
#     @classmethod
#     def specie2(cls):
#         return cls.specie

# # h1 = Human("uzair", 20)
# # h2 = Human("ali ", 30)
# # print(h1.name , h1.age , h1.myname())
# # # print(h2.name , h2.age , h2.specie,h2.specie2)


# # list

# Human.specie


class Car:
    Tax_price= 1000
    def __init__(self, price, year):
        self.price = price
        self.year = year
    def price2(self):
        return self.price 
    @classmethod
    def Tax(cls):
        return cls.Tax_price + 100
    @staticmethod
    def Total_price(): 
        return Car.Tax_price


c1 = Car(20000, 2020)

# print(c1.price , c1.year , c1.Tax_price)

print(c1.Total_price())
# c2 = Car(30000, 2021) 
# print(c2.price , c2.year , Car.Tax())



