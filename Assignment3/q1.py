import numpy as np
import matplotlib.pyplot as plt

time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

lambda_val = 0.3
R_case1 = np.exp(-lambda_val * time)

k_case2 = 0.9
R_case2 = np.exp(-0.5 * k_case2 * time**2)

m_case3 = 0.5
k_case3 = 0.9
integral_case3 = (k_case3 / (m_case3 + 1)) * (time**(m_case3 + 2) / (m_case3 + 2))
R_case3 = np.exp(-integral_case3)

print("=== Specific Reliability Values ===")
print(f"CASE I   (t = 3h): R(3) = {R_case1[2]:.6f}")
print(f"CASE II  (t = 5h): R(5) = {R_case2[4]:.6e}")
print(f"CASE III (t = 5h): R(5) = {R_case3[4]:.6e}\n")

print("=== Reliability Across All Time Points ===")
print(f"{'Time (h)':<10} | {'Case I':<12} | {'Case II':<12} | {'Case III':<12}")
print("-" * 52)
for t, r1, r2, r3 in zip(time, R_case1, R_case2, R_case3):
    print(f"{t:<10} | {r1:<12.5f} | {r2:<12.5e} | {r3:<12.5e}")

plt.figure(figsize=(10, 6))
plt.plot(time, R_case1, marker='o', linestyle='-', label='Case I')
plt.plot(time, R_case2, marker='s', linestyle='--', label='Case II')
plt.plot(time, R_case3, marker='^', linestyle='-.', label='Case III')

plt.title('Reliability vs. Time to Failure')
plt.xlabel('Time to Failure (hours)')
plt.ylabel('Reliability R(t)')
plt.xticks(time)
plt.grid(True, which='both', linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()