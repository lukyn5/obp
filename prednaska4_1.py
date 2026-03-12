from dataclasses import dataclass, field
import random

@dataclass
class User:
    name: str
    age: int
    _id: int = field(init=False, compare=False)

    def __post_init__(self):
        self._id = random.randint(1, 100000)

class User2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__post_int__()

    def __post_init__(self):
        self._id = random.randint(1, 10000)

    def __repr__(self):
        pass
        


if __name__ == '__main__':
    u1 = User("Alice", 18)
    u2 = User("Bob", 18)
    u3 = User("Charlie", 18)
    print(u3)

