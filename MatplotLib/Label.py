# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.plot(x,y)
# You can use the loc parameter in title() to position the title.
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

plt.title("Sport watch Data" , fontdict=font1, loc='left')
#You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.

plt.xlabel("Average Pulse", fontdict=font1)
plt.ylabel("Calorie Burnage" , fontdict=font2)

plt.show()