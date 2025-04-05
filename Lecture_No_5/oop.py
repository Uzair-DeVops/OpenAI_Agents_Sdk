class Human:
    def __init__(self, name, age, gender, nationality):
             # type: ignore
        self.name = name  # type: str
        self.age = age  # type: int
        self.gender = gender  # type: str
        self.nationality = nationality  # type: str
    def __repr__(self):
        return f" Human(name=%s, age=%s, gender=%s )" % (self.name, self.age, self.gender) # type: ignore  
    # def __str__(self):
    #     return f'{self.name} is {self.age} years old, a {self.gender} from {self.nationality}.'
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.gender == other.gender and self.nationality == other.nationality
    
    
    # def speak(self):
    #     return self.name , "is speaking"
    # def introduce_self(self):
    #     return f'Hi, my name is {self.name}. I am {self.age} years old, a {self.gender} from {self.nationality}.'


# print(dir(Human))

h1 = Human("uzair",20,"male","Pakistan")
h2 = Human("uzair",20,"male","Pakistan")
# print(h1.name)
# print()
# print(dir(h1))
print(h1) 