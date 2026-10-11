import pandas as pd
df=pd.read_csv('D:\\Python Prc & Environment\\python\\pandas\\panda.csv')

print(pd.options.display.max_rows) #60 rows shows

pd.options.display.max_rows=999