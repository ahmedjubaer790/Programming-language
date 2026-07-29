import pandas as pd
student=[{'ID':101,
         'NAME':'Jubaer',
         'DEPT':'IIT',
         'CGPA':3.67},

         {'ID':102,
         'NAME':'TEST',
         'DEPT':'IIT',
         'CGPA':3.67},

         {'ID':103,
         'NAME':'Jubaer',
         'DEPT':'IIT',
         'CGPA':3.67}
]

new=    {'ID':input('Type Id: '),
         'NAME':input('Type name: '),
         'DEPT':input('Type Dept: '),
         'CGPA':input('Type cg: ')
         }
student.append(new)
print(student)

search_opt=input('Search the name: ')

for s in student:
    if s['NAME']==search_opt:
        print(s)
    elif s['DEPT']==search_opt:
        print(s)
    elif s['CGPA']==search_opt:
        print(s)
    elif s['ID']==search_opt:
        print(s)    

df=pd.DataFrame(student)
df.to_excel('output.xlsx',index=False)