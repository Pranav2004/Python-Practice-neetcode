class Account:
    def __init__(self, title: str, balance: int):
        self.title = title   #public attribute
        self._balance = balance #protected attribute
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")   #not recommended to use a protected attribute outside the class


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
