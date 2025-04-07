# # instance variables
# # class variables or static variables
# # Instance functions 
# # class methods
# # static methods 
# from dataclasses import dataclass
# from typing import ClassVar

# @dataclass
# class Human:
#     # class variable
#     specie: ClassVar[str] = "HumanSpecie"
#     name: str
#     age: int
#     def myname(self):
#         return "my name is" , self.name , "and my specie is " , self.specie



# h1 = Human("uzair" , 20)

# # print(h1.myname())

# print(Human.specie  )

# class MyClass:
#     class_var = 10  # Class variable

#     def instance_method(self):
#         print("Before modification:", self.class_var)
#         # Assigning to self.class_var creates a new instance variable
#         self.class_var = 20
#         print("After modification:", self.class_var)

# obj = MyClass()
# obj.instance_method()  # Prints: 10 then 20

# # The class variable remains unchanged:
# print("Class variable remains:", MyClass.class_var)  # Output: 10

# # The instance now has its own attribute:
# print("Instance variable on obj:", obj.class_var)  # Output: 20
