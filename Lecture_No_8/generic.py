from typing import TypeVar , Generic , ClassVar
T = TypeVar('T')
from dataclasses import dataclass , field

# def return_item(a:list[T]) -> T:
#     return a[0]


# b = return_item([1,2,3])
# print(type(b)) # prints 1





@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)
    limit: ClassVar[int] = 10

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()