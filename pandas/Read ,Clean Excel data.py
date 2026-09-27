import pandas as pd
#for read file you need add the path
df=pd.read_csv('D:\\Python Prc & Environment\\python\\pandas\\panda.csv')
print(df)

#find missing values
missing_values=df.isnull().sum()
print(f"Missing values are: \n{missing_values}")

#count duplicate values
dupli_rows=df[df.duplicated()]
print(f"Duplicated values are \n{dupli_rows}")

num_duplicates = df.duplicated().sum()
print(f"Total duplicate rows count: {num_duplicates}\n")

#data clean
drop_dup=df.drop_duplicates()

#fiil up value
df['signup_date']=df['signup_date'].fillna('09-28-2026')
df['score']=df['score'].fillna(70)

#save clean data
df.to_csv('clean_data.csv', index=False)