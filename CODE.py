import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Inputs from the user
u = float(input("Enter the initial velocity u of the projectile (in m/s): "))
theta_deg1 = float(input("Enter the launch angle in degrees: "))
theta_deg2 = float(input("Enter the launch angle in degrees: "))
theta_deg3 = float(input("Enter the launch angle in degrees: "))
theta_deg4 = float(input("Enter the launch angle in degrees: "))
g = 9.8



# 2. Convert angle to radians for math functions
theta_rad1 = np.radians(theta_deg1)
theta_rad2 = np.radians(theta_deg2)
theta_rad3 = np.radians(theta_deg3)
theta_rad4 = np.radians(theta_deg4)

# 3. Calculating total Time of Flight 
# Total time = (2 * u * sin(theta)) / g...... formula ye h ..np =Numpy
t_flight1 = (2 * u * np.sin(theta_rad1)) / g
t_flight2 = (2 * u * np.sin(theta_rad2)) / g
t_flight3 = (2 * u * np.sin(theta_rad3)) / g
t_flight4 = (2 * u * np.sin(theta_rad4)) / g
#f is a formatted output of string aur last me jo 2f h means upto 2 decimals. 
#iska format h {variable:.number of decimalsf}
print(f"\n Total Time of Flight: {t_flight1:.2f} seconds")
print(f"\n Total Time of Flight: {t_flight2:.2f} seconds")
print(f"\n Total Time of Flight: {t_flight3:.2f} seconds")
print(f"\n Total Time of Flight: {t_flight4:.2f} seconds")


    
# 4. Generate 100 time points from 0 to the end of flight to make a smooth curve
t_points1 = np.linspace(0, t_flight1, 100)
t_points2 = np.linspace(0, t_flight2, 100)
t_points3 = np.linspace(0, t_flight3, 100)
t_points4 = np.linspace(0, t_flight4, 100)


# 5. Physics formulas for X (horizontal) and Y (vertical) positions
# Horizontal: x = u * cos(theta) * t
# Vertical:   y = u * sin(theta) * t - 0.5 * g * t^2
#cos(x)- Error (Python doesn't know what this is).
# math.cos(x) -Works,but only for one number at a time.
# np.cos(x) -Works perfectly for huge lists and arrays of numbers all at once, 
#mod is there taki wo graphs x ke niche na jae
#the comma in np.mod() separates its two arguments.(x,y)

X1 = (u * np.cos(theta_rad1) * t_points1)
Y1 = ((u * np.sin(theta_rad1) * t_points1) - (0.5 * g * t_points1**2))
X2 = (u * np.cos(theta_rad2) * t_points2)
Y2 = ((u * np.sin(theta_rad2) * t_points2) - (0.5 * g * t_points2**2))
X3 = (u * np.cos(theta_rad3) * t_points3)
Y3 = ((u * np.sin(theta_rad3) * t_points3) - (0.5 * g * t_points3**2))
X4 = (u * np.cos(theta_rad4) * t_points4)
Y4 = ((u * np.sin(theta_rad4) * t_points4) - (0.5 * g * t_points4**2))

fig, ax = plt.subplots(figsize=(8,5))
ax.set_xlim(0, max(X1.max(), X2.max(), X3.max(), X4.max()))
ax.set_ylim(0, max(Y1.max(), Y2.max(), Y3.max(), Y4.max())+2)


# 6. Plotting the results

#plt.figure(figsize=(8, 5))
#plt.plot((X1, Y1,), label="Projectile Path1", color="blue", linewidth=2)
#plt.plot((X2, Y2,), label="Projectile Path2", color="red", linewidth=2)
#plt.plot((X3, Y3,), label="Projectile Path3", color="green", linewidth=2)
#plt.plot((X4, Y4,), label="Projectile Path4", color="orange", linewidth=2)



# Graph styling
ax.set_title("Projectile Motion Trajectory")
ax.set_xlabel("Horizontal Distance (meters)")
ax.set_ylabel("Vertical Height (meters)")
ax.grid(True, linestyle="--", alpha=0.6)
ax.axhline(0, color='black', linewidth=1) # Ground line


line1, = ax.plot([], [], 'b', lw=2, label="Projectile Path")
line2, = ax.plot([], [], 'r', lw=2, label="Projectile Path")
line3, = ax.plot([], [], 'g', lw=2, label="Projectile Path")
line4, = ax.plot([], [], 'orange', lw=2, label="Projectile Path")
ax.legend()

def update(frame):
    if frame < len(X1):
        line1.set_data(X1[:frame], Y1[:frame])

    if frame < len(X2):
        line2.set_data(X2[:frame], Y2[:frame])

    if frame < len(X3):
        line3.set_data(X3[:frame], Y3[:frame])

    if frame < len(X4):
        line4.set_data(X4[:frame], Y4[:frame])

    return line1, line2, line3, line4
  #line.set_data(x[:frame], y[:frame])
    #return line,

ani = FuncAnimation(fig, update,
                    frames=max(len(X1), len(X2), len(X3), len(X4)),
                    interval=20,
                    blit=True)

ani.save("projectile_animation.gif", writer="pillow", fps=30)
# Or:
# ani.save("projectile_animation.mp4", writer="ffmpeg", fps=30)





#True: Enables the grid.
#linestyle="--" grid lines from solid to dashed.
#aplpha=0.6: Makes the grid lines slightly transparent.for total black its
# 1.0 and for total white its 0.0.
#plt.grid(True, linestyle="--", alpha=0.6)
#plt.axhline(0, color='black', linewidth=1) # Ground line
#plt.legend()

# Display the graph
plt.show()