import numpy as np
import matplotlib.pyplot as plt

# Data inputs
n_failures = np.array([59, 24, 29, 30, 17, 13])
N = 172
dt = 1000
t_start = np.array([0, 1000, 2000, 3000, 4000, 5000])
t_end = np.array([1000, 2000, 3000, 4000, 5000, 6000])
t_mid = (t_start + t_end) / 2

# Calculations
cum_failures = np.cumsum(n_failures)
N_start = N - np.insert(cum_failures[:-1], 0, 0)
R_end = (N - cum_failures) / N
F_end = cum_failures / N
f_val = n_failures / (N * dt)
z_val = n_failures / (N_start * dt)

# Setup subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# (a) Hazard Function z(t)
axs[0, 0].plot(t_mid, z_val, marker='o', color='crimson', linestyle='-')
axs[0, 0].set_title('(a) Hazard Function, z(t)')
axs[0, 0].set_xlabel('Operating Time (h)')
axs[0, 0].set_ylabel('z(t) [1/h]')
axs[0, 0].grid(True, linestyle=':', alpha=0.7)

# (b) Density Function f(t)
axs[0, 1].bar(t_mid, f_val, width=dt, color='darkorange', edgecolor='black', alpha=0.7)
axs[0, 1].set_title('(b) Density Function, f(t)')
axs[0, 1].set_xlabel('Operating Time (h)')
axs[0, 1].set_ylabel('f(t) [1/h]')
axs[0, 1].grid(True, linestyle=':', alpha=0.7)

# (c) Cumulative Distribution Function F(t)
t_points_c = np.insert(t_end, 0, 0)
F_points = np.insert(F_end, 0, 0)
axs[1, 0].plot(t_points_c, F_points, marker='s', color='teal', linestyle='-')
axs[1, 0].set_title('(c) Cumulative Distribution Function, F(t)')
axs[1, 0].set_xlabel('Operating Time (h)')
axs[1, 0].set_ylabel('F(t)')
axs[1, 0].set_ylim(-0.05, 1.05)
axs[1, 0].grid(True, linestyle=':', alpha=0.7)

# (d) Reliability Function R(t)
R_points = np.insert(R_end, 0, 1.0)
axs[1, 1].plot(t_points_c, R_points, marker='^', color='navy', linestyle='-')
axs[1, 1].set_title('(d) Reliability Function, R(t)')
axs[1, 1].set_xlabel('Operating Time (h)')
axs[1, 1].set_ylabel('R(t)')
axs[1, 1].set_ylim(-0.05, 1.05)
axs[1, 1].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()