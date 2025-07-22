# Playing with mpl animations
# Sine wave 
# AUTHOR Sven Schrodt
# SINCE 20250708


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

matplotlib.use('TkAgg')

items = 100
style = 'rx'

fig, ax = plt.subplots(1,1)

x2 = np.linspace(0, 2 * np.pi, items)
y2 = np.sin(x2 ** 3)
plt.plot(x2, y2, '--')

x = np.linspace(0, 2*np.pi, items)
y = np.sin(x)


ax.set_xlim([0, 2*np.pi])
ax.set_ylim([-1.1, 1.1])

plt.plot(x, y , 'b-')
plt.plot(x, y *0.8, 'g--')
sinegraph, = ax.plot([], [], style)

 


def sine_step(i):
    """ Iterating x,y by each function call,
        adding data to sinegraph and plotting

    Args:
        i (_type_): iteration variable
    """
    sinegraph.set_data(x[:i],y[:i])
    ax.plot(x[i], y[i], markersize=3)
    

anim = animation.FuncAnimation(fig, sine_step, frames=len(x), interval=50)
plt.show()