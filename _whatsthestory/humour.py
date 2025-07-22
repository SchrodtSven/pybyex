# plot xkcd style xkcd.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)

with plt.xkcd():
    fig, ax = plt.subplots()
    ax.plot(x, y)

    fig.savefig("example.png")
    plt.show()
    
  
    