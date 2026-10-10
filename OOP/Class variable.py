# Problem 4: Class Variable

# Student নামে একটি class বানাও। এতে একটি class variable school_name = "Dhaka Model School" এবং একটি class variable total_students = 0 থাকবে।
# __init__(self, name, marks) এ marks একটি list। প্রতিবার নতুন object তৈরি হলে total_students ১ করে বাড়বে।
# average(self) method গড় নম্বর return করবে।
# grade(self) method return করবে: গড় ≥ 80 হলে “A”, ≥ 60 হলে “B”, ≥ 40 হলে “C”, নইলে “F”।


class Student:
    school_name="Dhaka Model School"
    total_students=0

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_students+=1

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg=self.average()
        if avg>=80:
            return "A"
        elif avg>=60 and avg<80:
            return "B"
        
        elif avg>=40 and avg<60:
            return "C"
        else:
            return "F" 


s1=Student("Jubaer",[80,90,70])
s2=Student("Israt",[10,20,30])

print(s1.name,s1.average(),s1.grade())

print(s2.name,s2.average(),s2.grade())

print(Student.total_students)

    
        