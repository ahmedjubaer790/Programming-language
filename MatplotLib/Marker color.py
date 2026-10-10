# Marker Color
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,6,8])
y=np.array([3,8,1,10])

plt.plot(x,y, label="Many points", linestyle='--', color='g', marker='o', mec='k', ms=20)
plt.title("Multiple Line")
plt.legend() #for showing label
plt.show()