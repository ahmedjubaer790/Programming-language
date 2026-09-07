class pal:
    def sol(self,x:int)->bool:
        return str(x)==str(x)[::-1]

s=pal()

print(s.sol(121))

#2nd method
class sol2:
    def __init__(self,x:int):
        self.x=x

    def sol(self)->bool:
        return str(self.x)==str(self.x)[::-1]
s=sol2("121")
print(s.sol())   
