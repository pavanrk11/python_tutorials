# Most powerful, extensive .. data visualization/plotting library
# in python

import matplotlib.pyplot as plt
import numpy as np

# object hierarchy : tree-like structure of matplotlib objects underlying each plot
# the Figure object as a box-like container holding one or more Axes (actual plots)
# the Axes in the hierarchy are smaller objects such as tick marks, individual lines, legends, and text boxes

# fig, _ = plt.subplots()
# help(plt.subplots())

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.

fig = plt.figure()             # an empty figure with no Axes
fig, ax = plt.subplots()       # a figure with a single Axes
fig, axs = plt.subplots(nrows=2, ncols=2)  # a figure with a 2x2 grid of Axes
type(ax)
ax
ax.shape
fig.axes[0]
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
ax1, ax2, ax3, ax4 = ax.flatten()  # flatten a 2d NumPy array to 1d

gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))

# a figure with one Axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])

# line plot
x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the Axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the Axes.
ax.set_ylabel('y label')  # Add a y-label to the Axes.
ax.set_title("Simple Plot")  # Add a title to the Axes.
ax.legend()  # Add a legend.

# customize as per your needs
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

# color and styling
fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')

# axis labels, text
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# the histogram of the data
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)

# annotations
fig, ax = plt.subplots(figsize=(5, 2.7))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_ylim(-2, 2)

# legends
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(np.arange(len(data1)), data1, label='data1')
ax.plot(np.arange(len(data2)), data2, label='data2')
ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
ax.legend()

# ticks and formatters
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, data1)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title('Manual ticks')

# interactive mode

# Matplotlib interacts with different backends to render a chart.
# These backends help dynamically to update and “pop up” to the user when something's is changed

plt.rcParams['interactive']  # or: plt.isinteractive()

plt.ioff()
plt.ion()

# If interactive mode is on, you don’t need plt.show(), and images will automatically pop-up and be updated
# as you reference them.

# If interactive mode is off, you’ll need plt.show() to display a figure and plt.draw() to update a plot.

import matplotlib.pyplot as plt

# Enable interactive mode
plt.ion()

# Example plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]
plt.plot(x, y)
plt.title("Interactive Plot")
plt.show()

# Update plot in real time
for i in range(6, 11):
    x.append(i)
    y.append(y[-1] + 5)
    plt.plot(x, y)  # Re-plot with new data
    plt.pause(0.5)  # Pause to see updates

# using widgets

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial data
x = [i for i in range(100)]
y = [i**2 for i in x]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Space for the slider
line, = ax.plot(x, y, label="y = x^2")
ax.legend()

# Slider widget
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])  # x, y, width, height
slider = Slider(ax_slider, 'Power', 1, 3, valinit=2)

# Update function
def update(val):
    power = slider.val
    line.set_ydata([i**power for i in x])
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()

# using event handlers
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([0, 1, 2], [0, 1, 4], label="Click to see coords")
ax.legend()

# Define event handler
def on_click(event):
    if event.xdata and event.ydata:  # Ensure click is inside the plot
        print(f"Clicked at: ({event.xdata:.2f}, {event.ydata:.2f})")

fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
