import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('D:\\Python Prc & Environment\\python\\Matplot and Pandas Exercise\\company_sales_data.csv')

total_units=df['total_units'].tolist()
month=df['month_number'].tolist()

face_cr=df['facecream'].tolist()
face_wash=df['facewash'].tolist()
toothPaste=df['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot(month,face_cr, label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(month, face_wash,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(month, toothPaste, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(month, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(month, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(month, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.ylabel('Total Sold Units')
plt.xlabel('Month')
plt.legend()
plt.show()