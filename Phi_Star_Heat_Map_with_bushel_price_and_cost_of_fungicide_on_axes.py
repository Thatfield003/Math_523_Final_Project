import numpy as np
import matplotlib.pyplot as plt

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
theta = 0.3
seed = 250000
d_values = np.linspace(0.0, 0.13, 50)
b_values = np.linspace(10, 20, 10)
phi_values = np.linspace(0.01, 0.65, 100)

# Initialize an empty matrix to store phi* values
phi_star_matrix = np.zeros((len(b_values), len(d_values)))

# Calculate phi* for each combination of d and b
for i, d in enumerate(d_values):
    for j, b in enumerate(b_values):
        p_matrix = np.zeros(len(phi_values))
        for k, phi in enumerate(phi_values):
            p_matrix[k] = get_timeseries_profit(x0, phi, r, kappa, beta, seed, T, d)
        phi_star_matrix[j, i] = phi_values[np.argmax(p_matrix)]

# Create the heatmap
plt.figure(figsize=(10, 6))
plt.imshow(phi_star_matrix, cmap='hot', interpolation='nearest',
           origin='lower', aspect='auto')
plt.colorbar(label='phi*')

if len(d_values) > 10:
    plt.xticks(np.arange(0, len(d_values), len(d_values)//10),
               np.around(d_values[np.arange(0, len(d_values), len(d_values)//10)], 2))
else:
    plt.xticks(np.arange(0, len(d_values)),
               np.around(d_values, 2))
   
if len(b_values) > 10:
    plt.yticks(np.arange(0, len(b_values), len(b_values)//10),
               np.around(b_values[np.arange(0, len(b_values), len(b_values)//10)], 1))
else:
    plt.yticks(np.arange(0, len(b_values)),
               np.around(b_values, 1))

plt.xlabel('d')
plt.ylabel('b')
plt.title('Heatmap of phi* with d on the x-axis and b on the y-axis')
plt.show()
