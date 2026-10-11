#for date and time
import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())


# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value,
# and we can remove the row by using the dropna() method.

# Remove rows with a NULL value in the "Date" column:

df.dropna(subset=['Date'], inplace = True)