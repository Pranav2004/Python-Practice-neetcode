class PasswordManager:
    def __init__(self, password: str):
        self._password = password   # private attribute
        
    
    # TODO: Implement the verify_password method
    def verify_password(self, my_password: str):
        if my_password == self._password:
            return True
        else:
            return False
         



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
