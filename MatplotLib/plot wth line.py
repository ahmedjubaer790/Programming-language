# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'
# Plotting Without Line

import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,3])
ypoint=np.array([8,10])

plt.plot(xpoints,ypoint,'o')
plt.show()