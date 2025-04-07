from dataclasses import dataclass 
from typing import ClassVar

# @dataclass(unsafe_hash=True , order=True)
# class User:
#     """Class representing a user."""
#     human: str = "human"  # Class variable


#     name: str
#     age: int



#      # type: ignore
# U1 = User("uzair", 22)
# U2 = User("uzair", 20)

# print(User.name)
# # print(U1.age)
# # U1.age = 30
# # print(U1.age)


# # class User:
# #     """Class representing a user."""
# #     def __init__(self, name: str, age: int) -> None:
# #         self.name = name
# #         self.age = age
# #     def __eq__(self, other: object) -> bool:
# #         if not isinstance(other, User):
# #             return NotImplemented
# #         return self.name == other.name and self.age == other.age
# #     def __lt__(self, other: object) -> bool:
# #         if not isinstance(other, User):
# #             return NotImplemented
# #         return self.age < other.age

# # U1 = User("uzair", 20)
# # U2 = User("uzair", 10)
# # print(U1 < U2)  # Uncommenting this line will raise an error


# from dataclasses import dataclass

# @dataclass
# # class Car:
# #     brand: CLASSstr = "Corolla"

# #     color: str 
# #     price: int = 20000
# # c1 = Car( "red")
# # print(c1)  # Output: Corolla

@dataclass()  # Making the class immutable and orderable
class User:
    specie: ClassVar[str] = "human"  # Class variable
    name: str
    age: int

    def change(self):
        self.specie = "animal"  # Changing the class variable
        return self.specie

    @classmethod
    def change_specie(cls):
        cls.specie = "mustafa"
        return cls.specie
    
u1 = User("uzair", 22)
print("before changing" , User.specie)

print("after changing" , u1.change_specie())  # Output: human


print("class variable remain same" , User.specie)

