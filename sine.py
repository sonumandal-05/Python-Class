import matplotlib.pyplot as plt
import numpy as np

x= np ,pinespace (0,2*np.pi,100)
sine=np.sin(x)
plt.plot(x,sine,linestyle='dashed',color='red',linewidth=2)
plt.xlabel('Angel in radians')
plt.ylabel('Y-axis',fontsize=14)
plt.title('Sine Wave',fontsize=16)
plt.grid()
plt.axhline()
plt.show()