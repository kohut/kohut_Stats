import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

def IP10k_CIs(num_events, num_miles, ci_width):
    alpha = 1 - ci_width
    lower_ci = (gamma.ppf(alpha/2, num_events, 1) - 1) / num_miles
    upper_ci = (gamma.ppf(1-alpha/2, num_events+1, 1) - 1) / num_miles

    IP10k_lower_ci = lower_ci * 10000
    IP10k_upper_ci = upper_ci * 10000

    return [IP10k_lower_ci, IP10k_upper_ci]

def plot_CIs(num_events, mileage_sweep, ci_width):
    IP10k_ci_list = []
    for miles in mileage_sweep:
        IP10k_ci = IP10k_CIs(num_events, miles, ci_width)
        IP10k_ci_list.append(IP10k_ci)

    plt.plot(mileage_sweep, IP10k_ci_list)
    plt.show()

plot_CIs(1, np.linspace(3000, 15000, num = 30), 0.95)
