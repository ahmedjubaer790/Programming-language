# Color Syntax	Description
# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White


import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,6,8])
y=np.array([3,8,1,10])

plt.plot(x,y, label="Many points", linestyle='--', color='g')
plt.title("Multiple Line")
plt.legend() #for showing label
plt.show()