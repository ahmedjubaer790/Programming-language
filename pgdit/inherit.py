class person:
    species="student"
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname) #parent class
        self.grd=year
x=student("Jubaer","Ahmed",2024)
x.printname()
        


        