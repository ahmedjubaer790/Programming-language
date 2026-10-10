class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount

    
    def get_details(self):
        self.new_blance=self.balance+self.amount
        print(f"Account Holder:[{self.account_holder}], Blance: $[{self.new_blance}]")

bk=BankAccount("Jubaer Ahmed",5000)

bk.deposit(2000)


bk.get_details()
