# Draw a line in a diagram from position (1, 3) to position (8, 10):
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,3])
ypoints=np.array([8,10])

plt.plot(xpoints,ypoints)
plt.show()