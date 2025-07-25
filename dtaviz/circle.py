from matplotlib import pyplot as plt, animation as an
import numpy as np

fig = plt.figure()
board = plt.axes(xlim=(0, 200), ylim=(0, 100))

x = 10
y = 10
r = 10

for p in range(10):
    circle = plt.Circle((x, y), r, fc='w', ec='b')
    board.add_patch(circle)

    annotation = plt.annotate("", xytext=(x, y), xy=(x+10, y+10), arrowprops=dict(facecolor='r', edgecolor='r', headwidth=6, headlength=6, width=0.1))

    plt.draw()
    plt.pause(0.2)
    circle.remove()
    annotation.remove()
    x += 10
    y += 10

plt.show()