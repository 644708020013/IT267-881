class Account:
    def __init__(self) -> None:
        self.type = ''
        self.number = ''
        self.balance = 0
   
    def open_account(self,name,type,number,balance):
        self.name = name
        self.type = type
        self.number = number
        self.balance = balance
   
    def display_balance(self):
        return f'{self.name}\'s account balance = {self.balance} baht'
