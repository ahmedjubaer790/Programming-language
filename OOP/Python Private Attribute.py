class account:
    def __init__(self,account_nm,blance):
        self.account_nm="Jubaer Ahmed"
        self.blance=5000

class deposit(account):
    def __init__(self, account_nm, blance,deposit):
        super().__init__(account_nm, blance)

        self.deposit=deposit
        afterDipo=self.blance+self.deposit

d=deposit("anything",2000,3000)
print(d.account_nm)
print(d.blance)
print(d.deposit)        