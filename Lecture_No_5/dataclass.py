from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int
    gender: str
    nationality: str

h1 = Human("uzair",20,"male","Pakistan")
h2 = Human("uzair",20,"male","Pakistan")
print(h1)