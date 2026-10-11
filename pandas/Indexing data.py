# Create a simple Pandas DataFrame:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df=pd.DataFrame(data,index=["day 1","day 2","day 3"])


print(df)

#refer to the named index:
print(df.loc["day 2"])

