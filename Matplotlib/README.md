
# Matplotlib - A Complete Guide

This README provides a comprehensive guide to `Matplotlib`, a powerful plotting library in Python. It covers basic, advanced, and professional-level topics to help you master the art of data visualization.

## Table of Contents

1. [Installation](#installation)
2. [Basic Plotting](#basic-plotting)
3. [Customization](#customization)
4. [Advanced Topics](#advanced-topics)
5. [Handling Multiple Plots](#handling-multiple-plots)
6. [Working with DataFrames](#working-with-dataframes)
7. [Interactive Features](#interactive-features)
8. [Saving Plots](#saving-plots)
9. [Polar Plots and Heatmaps](#polar-plots-and-heatmaps)
10. [Combining with Other Libraries](#combining-with-other-libraries)
11. [Animations](#animations)

---

## Installation

To install `Matplotlib`, use the following pip command:

```bash
pip install matplotlib
```

---

## Basic Plotting

### Line Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

---

## Customization

### Customize Titles, Labels, and Grid

```python
plt.plot(x, y)
plt.title("Customized Line Plot", fontsize=14)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)
plt.grid(True)
plt.show()
```

---

## Advanced Topics

### Subplots

```python
fig, ax = plt.subplots(2, 1, figsize=(6, 8))

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 2, 3]

ax[0].plot(x, y1, color='blue')
ax[0].set_title("First Plot")

ax[1].bar(x, y2, color='orange')
ax[1].set_title("Second Plot")

plt.tight_layout()
plt.show()
```

### Log Scale and Inverse Axis

```python
plt.plot(x, y1)
plt.xscale('log')
plt.yscale('log')
plt.gca().invert_yaxis()
plt.show()
```

---

## Handling Multiple Plots

### Multiple Plots on One Figure

```python
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1)
axs[0, 1].bar(x, y2)
axs[1, 0].scatter(x, y2)
axs[1, 1].pie(y1, labels=x)

fig.suptitle("Multiple Plots")
plt.tight_layout()
plt.show()
```

### Inset Plot (Zoom-in Area)

```python
fig, ax = plt.subplots()
ax.plot(x, y1)

# Create an inset plot
inset = fig.add_axes([0.5, 0.5, 0.35, 0.35])
inset.plot(x, y1)
inset.set_xlim(2, 5)
inset.set_ylim(4, 25)
inset.set_title("Zoom-in View")
plt.show()
```

---

## Working with DataFrames

### Plot from Pandas DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    'Day': ['Sunday', 'Monday', 'Tuesday'],
    'Sales': [100, 200, 150]
})

df.plot(x='Day', y='Sales', kind='bar', color='skyblue', legend=False)
plt.title("Sales Data")
plt.ylabel("Sales")
plt.show()
```

---

## Interactive Features

### Handling Mouse Clicks

```python
def on_click(event):
    print(f"Clicked at x={event.xdata:.2f}, y={event.ydata:.2f}")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
```

---

## Saving Plots

### Save Plots as Image or PDF

```python
plt.plot(x, y1)
plt.savefig("plot.png")
plt.savefig("plot.pdf")
```

---

## Polar Plots and Heatmaps

### Polar Plot

```python
theta = np.linspace(0, 2*np.pi, 100)
r = np.abs(np.sin(5 * theta))

ax = plt.subplot(projection='polar')
ax.plot(theta, r)
ax.set_title("Polar Plot")
plt.show()
```

### Heatmap

```python
matrix = np.random.rand(5, 5)

fig, ax = plt.subplots()
cax = ax.imshow(matrix, cmap='coolwarm')

# Add color bar
fig.colorbar(cax)
ax.set_title("Heatmap")
plt.show()
```

---

## Combining with Other Libraries

### Integration with NumPy

```python
import numpy as np

t = np.linspace(0, 2*np.pi, 400)
s = np.sin(t)

plt.plot(t, s, label='sin(t)')
plt.plot(t, np.cos(t), label='cos(t)')
plt.title("Sinusoidal Functions")
plt.legend()
plt.grid(True)
plt.show()
```

---

## Animations

### Simple Animation

```python
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x, y = [], []
line, = ax.plot([], [], 'r-')

def update(frame):
    x.append(frame)
    y.append(frame**2)
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    return line,

ani = FuncAnimation(fig, update, frames=range(10), blit=True)
plt.show()
```

