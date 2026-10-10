# Exercise 1: Read Total profit of all months and show it using a line plot

# Total profit data provided for each month. Generated line plot must include the following properties: –

# X label name = Month Number
# Y label name = Total profit

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('D:\\Python Prc & Environment\\python\\Matplot and Pandas Exercise\\company_sales_data.csv')

profitlist=df['total_profit'].tolist()
month=df['month_number'].tolist()

plt.plot(month,profitlist, linestyle='dotted', label='Profit data of the last year', linewidth=3, color='r', marker='o', mec='g' )

plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.title('Total Profits of all months')
plt.legend(loc='lower right')

plt.show()