
class OldPrinter:
    def print_text(self, text):
        print(f"Tisknu na stare tiskarne: {text}")


class Printer:
    def print(self, message):
        print(f"tisknu na nove tiskarne: {message}")
        

class Adapter:
    def __init__(self):
        self.old_printer = OldPrinter()

    def print(self, message):
        self.old_printer.print_text(message)


 

if __name__ == "__main__":
    old_printer = OldPrinter()

    printer = Printer(adapter)
    printer.print("Hello, World!")

    adapter_na_starou_tiskarnu = Adapter(old_printer)