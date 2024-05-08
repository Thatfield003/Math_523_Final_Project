import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_cumulativeProfit(phi, r, kappa, beta, seed, c, theta, m, d):
    m_star = (beta*seed/kappa)*(1-(1/((1-phi)*r)))
    profit = (c*beta*seed)*(1-theta*(m/m_star)) - d*phi*beta*seed
    return profit

def get_timeseries_profit(x0, phi, r, kappa, beta, seed, T, d):
    x = [x0]
    x_old = x0
    profit = get_cumulativeProfit(phi, r, kappa, beta, seed, c, theta, x0, d)
    for i in range(T):
        x_new = (1-phi)*r*x_old*(1-kappa*(x_old/(beta*seed)))
        x.append(x_new)
        profit += get_cumulativeProfit(phi, r, kappa, beta, seed, c, theta, x_new, d)
        x_old = x_new
    return profit

# Parameters
x0 = 0.1
r = 3
kappa = 1000
beta = 0.81
T = 10
c = 12*100*50/(125000)  # or c = 100*50/(125000)
theta = 1
d_values = np.linspace(0.0, 0.41, 10)
b_values = np.linspace(10, 20, 10)
seed_values = np.linspace(125000, 250000, 10)
phi_values = np.linspace(0.01, 0.65, 100)

# Initialize an empty matrix to store phi* values
phi_star_matrix = np.zeros((len(b_values), len(d_values), len(seed_values)))

# Calculate phi* for each combination of b, d, and seed
for i, d in enumerate(d_values):
    for j, b in enumerate(b_values):
        for k, seed in enumerate(seed_values):
            p_matrix = np.zeros(len(phi_values))
            for l, phi in enumerate(phi_values):
                p_matrix[l] = get_timeseries_profit(x0, phi, r, kappa, beta, seed, T, d)
            phi_star_matrix[j, i, k] = phi_values[np.argmax(p_matrix)]

# Create the 3D plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Create grid for x, y, z
D, B, S = np.meshgrid(d_values, b_values, seed_values)

# Plot the surface
surf = ax.scatter(D, B, S, c=phi_star_matrix.flatten(), cmap='hot')
fig.colorbar(surf, label='phi*')

# Set labels and title
ax.set_xlabel('d')
ax.set_ylabel('b')
ax.set_zlabel('Seed')
ax.set_title('Optimal phi* with variable d, b, and Seed')

plt.show()
