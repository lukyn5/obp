# vytvorte singleton, ktery loguje do souboru

class Logger:

    _instance = None

    def __new__(cls, log_file=None):
        if cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._log_file = log_file
        return cls._instance

    def log(self, message):
        with open(self._log_file, "a") as f:
            print(f"zapisuji do souboru {self._log_file}: {message}")
            f.write(message + "\n")


if __name__ == "__main__":
    logger1 = Logger("log1.txt")
    logger2 = Logger("log2.txt")

    logger1.log("Hello from logger1")
    logger2.log("Hello from logger2")