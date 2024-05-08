import numpy as np
import matplotlib.pyplot as plt

def get_cumulativeProfit(phi, r, kappa, beta, seed, c, theta, m, b):
    m_star = (beta*seed/kappa)*(1-(1/((1-phi)*r)))
    profit = b*(c*beta*seed)*(1-theta*(m/m_star)) - d*phi*beta*seed

    return profit

def get_timeseries_profit(x0, phi, r, kappa, beta, seed, T, b):
    x = [x0]
    x_old = x0

    profit = get_cumulativeProfit(phi, r, kappa, beta, seed, c, theta, x0, b)

    for i in range(T):
        x_new = (1-phi)*r*x_old*(1-kappa*(x_old/(beta*seed)))
        x.append(x_new)
        profit += get_cumulativeProfit(phi, r, kappa, beta, seed, c, theta, x_new, b)
        x_old = x_new

    return profit

#heat map of profit over 10 years, with variable phi rates and d rates (cost of application of funcicide)
x0 = 0.1
r = 3
kappa = 1000
beta = 0.81
T = 10
#c = 12*100*50/(125000)
#c=12/50
c = 100*50/(125000)
theta = 0.3
d = 0.0395
seed = 250000
seed_values = np.linspace(125000,250000,2)
phi_values = np.linspace(0.01,0.65,100)
b_values = np.linspace(10,20,100)

# Initialize an empty matrix to store m_star values
p_matrix = np.zeros((len(phi_values), len(b_values)))

# Calculate m_star for each combination of r and kappa
for i, phi in enumerate(phi_values):
    for j, b in enumerate(b_values):
        p = get_timeseries_profit(x0, phi, r, kappa, beta, seed, T, b)
        p_matrix[i, j] = p

# Create the heatmap
plt.figure(figsize=(10, 6))
plt.imshow(p_matrix, cmap='hot', interpolation='nearest',
           origin='lower', aspect='auto')
plt.colorbar(label='p')

for j, b_val in enumerate(b_values):
    max_profit_index = np.argmax(p_matrix[:-1, j])  # Exclude phi = 0.5 values
    max_profit = p_matrix[max_profit_index, j]
    plt.scatter(j, max_profit_index, color='blue', marker='x', s=50)
    #plt.text(j, max_profit_index, f'{max_profit:.2f}', color='white', ha='center', va='center')


if len(b_values) > 10:
    plt.xticks(np.arange(0, len(b_values), len(b_values)//10),
               np.around(b_values[np.arange(0, len(b_values), len(b_values)//10)], 1))
else:
    plt.xticks(np.arange(0, len(b_values)),
               np.around(b_values, 1))
   
if len(phi_values) > 10:
    plt.yticks(np.arange(0, len(phi_values), len(phi_values)//10),
               np.around(phi_values[np.arange(0, len(phi_values), len(phi_values)//10)], 1))
else:
    plt.yticks(np.arange(0, len(phi_values)),
               np.around(phi_values, 1))

plt.xlabel('b')
plt.ylabel('phi')
plt.title('Heatmap of profit')
plt.show()
