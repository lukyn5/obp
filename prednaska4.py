from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: int = 1000
    tag: list = field(default_factory=list)

class Product2:
    def __init__(self, name, price=1000, tag=[]):
        self.name = name
        self.price = price
        self.tag = tag

    def __repr__(self):
        return f"Product2: name={self.name}, price={self.price}, tag={self.tag}"
    

if __name__ == "__main__":
    p1 = Product2("Zubni pasta")
    print(p1)
    p2 = Product2("Pasta")
    print(p2)
    p2.tag.append("matova")
    print(p2)
    print(p1)