# Projectile Motion Animation

## Overview

This project is a Python-based simulation of projectile motion. It takes the initial velocity and four different launch angles as input and calculates the trajectory of each projectile.

The project uses NumPy for numerical calculations and Matplotlib for plotting and creating an animated visualization of the projectile paths.

## Features

- Takes initial velocity as user input.
- Takes four different launch angles as input.
- Calculates the total time of flight for each projectile.
- Calculates horizontal and vertical positions using projectile-motion equations.
- Generates smooth projectile trajectories using NumPy arrays.
- Displays four projectile paths on the same graph.
- Creates an animated visualization of the motion.
- Saves the animation as a GIF file.

## Technologies Used

- Python
- NumPy
- Matplotlib
- Matplotlib Animation (`FuncAnimation`)
- Pillow

## Physics Used

The simulation is based on standard projectile-motion equations.

### Time of Flight

For a projectile launched from ground level:

```text
T = (2u sin(theta)) / g
where:

u = initial velocity
theta = launch angle
g = acceleration due to gravity (9.8 m/s²)
Horizontal Position
x = u cos(theta) t
Vertical Position
y = u sin(theta) t - 1/2 gt²

The angle entered by the user in degrees is converted to radians before applying NumPy's trigonometric functions.