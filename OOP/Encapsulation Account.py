# Problem 5: Encapsulation

# SecureAccount class এ holder (public) এবং __balance (private) attribute থাকবে। balance এর default মান 0.0।
# @property দিয়ে balance পড়ার ব্যবস্থা করো (setter থাকবে না)।
# deposit(self, amount): amount ≤ 0 হলে ValueError("Deposit amount must be positive") raise করবে, নইলে balance বাড়িয়ে নতুন balance return করবে।
# withdraw(self, amount): amount > balance হলে ValueError("Insufficient balance") raise করবে, নইলে balance কমিয়ে নতুন balance return করবে।

class SecureAccount:
    def __init__(self,holder,__blance=0.0):
        self.holder=holder
        self.__blance=__blance
    @property
    def blance(self):
        return self.__blance

    def deposit(self,amount):
        if amount<0:
            raise ValueError ("Deposit amount must be positive")
        self.__blance+=amount
        return self.__blance

    def withdraw(self,amount):
        if amount>self.__blance:
            raise ValueError ("Insufficient blance")
        self.__blance-=amount
        return self.__blance

acc=SecureAccount("Jubaer Ahmed",1000)

print(acc.deposit(500))
print(acc.withdraw(300))
print(acc.blance)

try:
    acc.withdraw(5000)
except ValueError as e:
    print("Error :" ,e)




        