class BankAccount:
    def __init__(self,account_holder,blance=0.0):
        self.account_holder=account_holder
        self.blance=blance

    def deposit(self,amount):
        self.blance+=amount
        return self.blance

    def get_details(self):
        return f"Account Holder[{self.account_holder}] Blance: $[{self.blance}]"

    
bk=BankAccount("Jubaer Ahmed",5000)
bk.deposit(2000)
print(bk.get_details())