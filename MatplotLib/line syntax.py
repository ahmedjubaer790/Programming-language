# Line Syntax	Description
# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,6,8])
y=np.array([3,8,1,10])

plt.plot(x,y, label="Many points", linestyle='--' , color='r')
plt.title("Multiple Line")
plt.legend() #for showing label
plt.show()