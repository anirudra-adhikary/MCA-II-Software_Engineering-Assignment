import numpy as np
import matplotlib.pyplot as plt

# Given operating times
t = np.array([8, 20, 34, 46, 63, 86, 111, 141, 186, 266])
N = len(t)

# Calculate intervals and risk counts
t_prev = np.insert(t[:-1], 0, 0)
dt = t - t_prev
n_at_risk = np.arange(N, 0, -1)

# Calculations
R = (N - np.arange(1, N + 1)) / N
F = np.arange(1, N + 1) / N
f = 1.0 / (N * dt)
z = 1.0 / (n_at_risk * dt)

# Plotting the 4 quantities
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# (a) Hazard Function z(t)
axs[0, 0].plot(t, z, marker='o', color='crimson', linestyle='-')
axs[0, 0].set_title('(a) Hazard Function, z(t)')
axs[0, 0].set_xlabel('Operating Time (h)')
axs[0, 0].set_ylabel('z(t) [1/h]')
axs[0, 0].grid(True, linestyle=':', alpha=0.7)

# (b) Density Function f(t)
axs[0, 1].plot(t, f, marker='s', color='darkorange', linestyle='-')
axs[0, 1].set_title('(b) Density Function, f(t)')
axs[0, 1].set_xlabel('Operating Time (h)')
axs[0, 1].set_ylabel('f(t) [1/h]')
axs[0, 1].grid(True, linestyle=':', alpha=0.7)

# (c) Cumulative Distribution Function F(t)
axs[1, 0].step(np.insert(t, 0, 0), np.insert(F, 0, 0), where='post', color='teal', linewidth=2)
axs[1, 0].scatter(t, F, color='teal')
axs[1, 0].set_title('(c) Cumulative Distribution Function, F(t)')
axs[1, 0].set_xlabel('Operating Time (h)')
axs[1, 0].set_ylabel('F(t)')
axs[1, 0].set_ylim(-0.05, 1.05)
axs[1, 0].grid(True, linestyle=':', alpha=0.7)

# (d) Reliability Function R(t)
axs[1, 1].step(np.insert(t, 0, 0), np.insert(R, 0, 1), where='post', color='navy', linewidth=2)
axs[1, 1].scatter(t, R, color='navy')
axs[1, 1].set_title('(d) Reliability Function, R(t)')
axs[1, 1].set_xlabel('Operating Time (h)')
axs[1, 1].set_ylabel('R(t)')
axs[1, 1].set_ylim(-0.05, 1.05)
axs[1, 1].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()