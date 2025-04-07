# instance variables
# class variables or static variables
# Instance functions 
# class methods
# static methods 
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Human:
    # class variable
    specie: ClassVar[str] = "HumanSpecie"
    # instance variable
    name: str
    age: int
    def myname(self, name):
        return "my name is" , self.name



print(Human.specie)