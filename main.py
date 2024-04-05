import numpy as np
import matplotlib.pyplot as plt

# Get model parameters from user
alpha = float(input("Enter alpha parameter: "))

# Initial condition
theta_initial = float(input("Enter initial angle (in radians): "))

# Time points
timesteps = int(input("Enter number of timesteps: "))

# Circle map function
def circle_map(theta, alpha):
    return theta + alpha - 2 * np.pi * np.floor((theta + alpha) / (2 * np.pi))

# Iterate the circle map
theta_values = [theta_initial]
for _ in range(timesteps):
    next_theta = circle_map(theta_values[-1], alpha)
    theta_values.append(next_theta)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(theta_values[:-1], theta_values[1:], '.', markersize=1)
plt.xlabel('θ(t)')
plt.ylabel('θ(t+1)')
plt.title('Circle Map: Phase Portrait')
plt.grid(True)
plt.show()
