# ------------------=----- Abstraction in Python OOP --------------------------
# Hide Internal Functionality from Users is called Abstraction


from abc import ABC, abstractmethod

class ATM(ABC):
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    # @abstractmethod
    def _get_balance(self):
        return self.__balance
    def _set_balance(self, balance):
        self.__balance = balance
    @abstractmethod
    def withdrawl(self, amount):
        pass
    @abstractmethod
    def deposite(self, amount):
        pass
    @abstractmethod
    def get_balance(self):
        pass
    

class ConcreteATM(ATM):
    def withdrawl(self, amount):
        if amount > self._get_balance():
            print("Insuficient Funds")
        else:
            new_balance = self._get_balance() -  amount
            self._set_balance(new_balance)

            print(
                f"withdrawal {amount}, "
                f"New Balance {self._get_balance()}"
            )

    def deposite(self, amount):

        new_balance = self._get_balance() + amount
        self._set_balance(new_balance)

        print(
            f"Deposited {amount}, "
            f"New Balance {self._get_balance()}"
        )

    def get_balance(self):
        return self.get_balance()

atm = ConcreteATM("1234", 10000)

atm.deposite(500)
atm.withdrawl(200)

print(atm._get_balance())