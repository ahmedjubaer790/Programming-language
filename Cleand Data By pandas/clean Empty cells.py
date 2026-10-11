import pandas as pd
df=pd.read_excel('D:\\Python Prc & Environment\\python\\Cleand Data By pandas\\health_data.xlsx')

newvar=df.dropna()

# print(df)
# If you want to change the original DataFrame, use the inplace = True argument:
df.dropna(inplace = True) 
print(newvar)
