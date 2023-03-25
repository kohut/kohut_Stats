import numpy as np
from scipy.stats import gamma

def IPM_CIs(num_events, num_miles, ci_width):
    alpha = 1 - ci_width
    lower_ci = (gamma.ppf(alpha/2, num_events, 1) - 1) / num_miles
    upper_ci = (gamma.ppf(1-alpha/2, num_events+1, 1) - 1) / num_miles

    IP10k_lower_ci = lower_ci * 10000
    IP10k_upper_ci = upper_ci * 10000

    return [IP10k_lower_ci, IP10k_upper_ci]


print(IPM_CIs(1, 15000, 0.95))