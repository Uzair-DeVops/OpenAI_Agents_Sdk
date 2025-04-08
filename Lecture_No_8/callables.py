from dataclasses import dataclass
# def sum(a,b):
#     return a + b

# print(dir(sum))

@dataclass
class Sum:
    a: int
    b: int
    def __call__(self):
        return self.a + self.b

s1 = Sum(1, 2)
print(dir(s1))

s1()