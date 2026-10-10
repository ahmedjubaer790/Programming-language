import pandas as pd 
import matplotlib.pyplot as plt 

df=pd.read_csv('D:\\Python Prc & Environment\\python\\Matplot and Pandas Exercise\\company_sales_data.csv')

total_sold=df['toothpaste'].tolist()
month=df['month_number'].tolist()

plt.scatter(month,total_sold, label='Tothpaste sales data' )

plt.xlabel('Number of Months')
plt.ylabel('Number of unit solds')
plt.legend()
plt.grid()
plt.show()