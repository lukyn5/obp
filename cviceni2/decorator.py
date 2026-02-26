from abc import ABC, abstractmethod

class MetodaNeniimplementovana(Exception):
    pass

def abstractmethod_decorator(func):
    def wrapper(*args, **kwargs):
        raise MetodaNeniimplementovana(f"Metoda '{func.__name__}' není implementována.")
    return wrapper

class AbstractClass(ABC):
    @abstractmethod
    def method(self):
         pass

class MyClass(AbstractClass):
    def method(self):
        print("Implementace metody")




if __name__ == "__main__":
    my_object = MyClass()
    my_object.method()