import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colormaps
 
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
scat = ax.scatter(x, y, c=y, cmap=colormaps.get_cmap('viridis'))
 
def update(frame):
    y = np.sin(x + frame / 100)
    scat.set_offsets(np.c_[x, y])
    scat.set_array(y)
    return scat,
 
ani = FuncAnimation(fig, update, frames=range(100), blit=True)
plt.show()