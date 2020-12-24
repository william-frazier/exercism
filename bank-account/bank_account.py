from threading import Lock

class BankAccount:
    def __init__(self):
        self.balance = None
        self.status = None
        self.lock = Lock()

    def get_balance(self):
        with self.lock:
            if self.status:
                return self.balance
            raise ValueError("This account isn't open.")

    def open(self):
        with self.lock:
            if self.status:
                raise ValueError("Account already opened.")
            self.balance = 0
            self.status = True

    def deposit(self, amount):
        with self.lock:
            if not self.status:
                raise ValueError("This account isn't opened yet.")
            if amount <= 0:
                raise ValueError("You must deposit more than $0")
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount and self.status and amount > 0:
                self.balance -= amount
            else:
                raise ValueError("There is an error. Is your account closed or are you withdrawing more money than you have available?")

    def close(self):
        with self.lock:
            if not self.status:
                raise ValueError("This account wasn't open to begin with.")
            self.status = False
