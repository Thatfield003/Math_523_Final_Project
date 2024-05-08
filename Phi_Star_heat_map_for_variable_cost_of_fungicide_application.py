"""
Mathematical Model of White Mold on Soybean Yield
Created by Tanner Byer and Tad Hatfield
Spring 2024
"""

import numpy as np
import matplotlib.pyplot as plt

x0 = 0.1
r = 4
kappa = 1500
beta = 0.81
T = 10
c = 12*100*50/(125000)
#c=12/50
theta = 0.3
d = 0.0395

seed_values = np.linspace(125000,250000,2)
phi_values = np.linspace(0.2,0.75,200)
d_values = (0.001, 0.20, 100)

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

# Initialize lists to store profits for different seed values
profits_125k = []
profits_250k = []

# Calculate profits for each phi value and seed value
for phi in phi_values:
    profit_125k = get_timeseries_profit(x0, phi, r, kappa, beta, seed_values[0], T, d)
    profit_250k = get_timeseries_profit(x0, phi, r, kappa, beta, seed_values[1], T, d)
    profits_125k.append(profit_125k)
    profits_250k.append(profit_250k)

# Plot the profits
plt.plot(phi_values, profits_125k, label='Seed = 125,000')
plt.plot(phi_values, profits_250k, label='Seed = 250,000')
plt.xlabel('Phi')
plt.ylabel('Profit')
plt.title('Profit vs Phi for Different Seed Values')
plt.legend()
plt.grid(True)
plt.show()

#heat map of profit over 10 years, with variable phi rates and d rates (cost of application of funcicide)
x0 = 0.1
r = 3
kappa = 1000
beta = 0.81
T = 10
c = 12*100*50/(125000)
#c=12/50
#c = 100*50/(125000)
theta = 0.3
d = 0.0395
seed = 250000
seed_values = np.linspace(125000,250000,2)
phi_values = np.linspace(0.01,0.65,100)
d_values = np.linspace(0.0, 0.45, 100)

# Initialize an empty matrix to store m_star values
p_matrix = np.zeros((len(phi_values), len(d_values)))

# Calculate m_star for each combination of r and kappa
for i, phi in enumerate(phi_values):
    for j, d in enumerate(d_values):
        p = get_timeseries_profit(x0, phi, r, kappa, beta, seed, T, d)
        p_matrix[i, j] = p

# Create the heatmap
plt.figure(figsize=(10, 6))
plt.imshow(p_matrix, cmap='hot', interpolation='nearest',
           origin='lower', aspect='auto')
plt.colorbar(label='p')

for j, d_val in enumerate(d_values):
    phi_filtered = np.logical_or(phi_values <= 0.5, phi_values >= 0.5)
    phi_indices = np.where(phi_filtered)[0]  # Get valid indices
    if len(phi_indices) > 0:
        max_profit_index = phi_indices[np.argmax(p_matrix[phi_indices, j])]
        max_profit = p_matrix[max_profit_index, j]
        plt.scatter(j, max_profit_index, color='blue', marker='x', s=50)
        #plt.text(j, max_profit_index, f'{max_profit:.2f}', color='white', ha='center', va='center')

if len(d_values) > 10:
    plt.xticks(np.arange(0, len(d_values), len(d_values)//10),
               np.around(d_values[np.arange(0, len(d_values), len(d_values)//10)], 1))
else:
    plt.xticks(np.arange(0, len(d_values)),
               np.around(d_values, 1))
   
if len(phi_values) > 10:
    plt.yticks(np.arange(0, len(phi_values), len(phi_values)//10),
               np.around(phi_values[np.arange(0, len(phi_values), len(phi_values)//10)], 1))
else:
    plt.yticks(np.arange(0, len(phi_values)),
               np.around(phi_values, 1))

plt.xlabel('d')
plt.ylabel('phi')
plt.title('Heatmap of profit')
plt.show()

