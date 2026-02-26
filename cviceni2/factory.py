from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment:
    def pay(self, amount):
        print(f"Zaplaceno {amount} kartou")

class CashPayment:
    def pay(self, amount):
        print(f"Zaplaceno {amount} hotově")



def payment_factor(payment_type):
    types = {
        "card": CardPayment(),
        "cash": CashPayment()
    }
    return types.get(payment_type)


class PaymentProcessor:
    def pay(self, payment_type, amount):
        obj = payment_factor.pay(payment_type)
        obj.pay(amount)

    


if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.pay("card", 100)
    processor.pay("cash", 200)
