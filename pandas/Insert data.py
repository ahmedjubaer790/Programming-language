import pandas as pd

x=[{"ID":101,
    "Name":"Jubaer Ahmed",
    "Dept":"IIT"},
{"ID":102,
  "Name":"Jubaer Ahmed",
  "Dept":"IIT"}
]

student={
    "ID":input('Enter the ID '),
    "Name":input('Enter the name '),
    "Dept":input('Enter the department name ')
}

#for append we have to use list.Tupple is immutable.Tuple dont accept append
x.append(student)
#convert the data to pandas data frame
df=pd.DataFrame(x)

df.to_excel("output1.xlsx", sheet_name="student", index=False)

print(x)