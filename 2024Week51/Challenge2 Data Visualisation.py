'''
Challenge 2: Data Visualization - Mandelbrot Set
Context: 
The Mandelbrot Set is a famous fractal that showcases complex numbers' behavior. Visualizing it is a classic computational challenge.

Tasks:
Implement a function that calculates the number of iterations for a point in the complex plane to escape a given bound.
Use NumPy to generate a 2D grid of points in the complex plane.
Use Matplotlib's imshow to visualize the Mandelbrot Set.

Expected Output:
A colorful visualization of the Mandelbrot Set with a title, color bar, and axis labels.
'''
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

SIZE = 10
axis = np.linspace(-SIZE, SIZE)
grid = np.meshgrid(axis, axis*1j)

c = 1
n = 20
z0 = np.zeros_like(grid, dtype=complex)
z_new = lambda z, c : z**2 + c 
z = np.zeros(n)
for i in range(n):
    z = z_new(z, c)