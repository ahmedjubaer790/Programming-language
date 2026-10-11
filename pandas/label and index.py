# With the index argument, you can name your own labels.

import pandas as pd

x=[1,3,4,5]

myvar=pd.Series(x,index=['a','b','c','d'])
print(myvar)

print(myvar['a'])