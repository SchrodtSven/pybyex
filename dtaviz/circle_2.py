import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25))
sun=plt.Circle((0,0),radius=0.3,facecolor='yellow')
ax.add_patch(sun)
earth = plt.Circle((0, -1), 0.15, fc='b')

def init():
    earth.center = (0, -1)
    ax.add_patch(earth)
    return earth,

def animate(i):
    x = np.cos(np.radians(i))
    y = np.sin(np.radians(i))
    earth.center = (x, y)
    return earth,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
#save as a gif
writergif = animation.PillowWriter(fps=30)
#anim.save('filename.gif',writer=writergif)

plt.show()