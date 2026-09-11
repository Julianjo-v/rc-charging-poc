import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0
VIH = 0.7 * V0

# R and C selected for the application in Part A
R_nominal = 82e3       # 82 kohm
C_nominal = 100e-9     # 100 nF
tolerance = 0.05       # +/-5%

# Calculate the fastest-case and slowest-case values
R_fast = R_nominal * (1 - tolerance)
R_slow = R_nominal * (1 + tolerance)

C_fast = C_nominal * (1 - tolerance)
C_slow = C_nominal * (1 + tolerance)

# Calculate release times
# t_release = -RC ln(1 - VIH/V0)

def t_release(R, C):
    return -R * C * np.log(1 - VIH / V0)

t_nominal = t_release(R_nominal, C_nominal)
t_fast = t_release(R_fast, C_fast)
t_slow = t_release(R_slow, C_slow)

# Print the results
print("Nominal values:")
print(f"R = {R_nominal / 1e3:.2f} kohm")
print(f"C = {C_nominal * 1e9:.2f} nF")
print(f"t_release = {t_nominal * 1e3:.2f} ms")

print("\nFastest case:")
print(f"R = {R_fast / 1e3:.2f} kohm")
print(f"C = {C_fast * 1e9:.2f} nF")
print(f"t_release = {t_fast * 1e3:.2f} ms")

print("\nSlowest case:")
print(f"R = {R_slow / 1e3:.2f} kohm")
print(f"C = {C_slow * 1e9:.2f} nF")
print(f"t_release = {t_slow * 1e3:.2f} ms")

# Create a time axis based on the slowest charging curve
t = np.linspace(0, 5 * t_slow, 500)

# Charging equation
def charging(t, R, C):
    tau = R * C
    return V0 * (1 - np.exp(-t / tau))

# Plot the three charging curves
fig, ax = plt.subplots()

# Nominal case: solid line
ax.plot(
    t,
    charging(t, R_nominal, C_nominal),
    color="black",
    linewidth=2.5,
    label=f"Nominal: R = {R_nominal/1e3:.0f} kohm, C = {C_nominal*1e9:.0f} nF"
)

# Fastest case: dashed line
ax.plot(
    t,
    charging(t, R_fast, C_fast),
    color="black",
    linestyle="--",
    linewidth=1.3,
    label=f"Fastest: R = {R_fast/1e3:.1f} kohm, C = {C_fast*1e9:.0f} nF"
)

# Slowest case: dash-dot line
ax.plot(
    t,
    charging(t, R_slow, C_slow),
    color="black",
    linestyle="-.",
    linewidth=1.3,
    label=f"Slowest: R = {R_slow/1e3:.1f} kohm, C = {C_slow*1e9:.0f} nF"
)

# VIH reference line
ax.axhline(
    VIH,
    linestyle=":",
    color="0.4",
    label=r"$V_{IH}$"
)

ax.grid(False)

ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")

ax.set_title(
    f"RC Charging with Component Tolerance "
    f"(R = {R_nominal/1e3:.0f} kohm, C = {C_nominal*1e9:.0f} nF)"
)

ax.legend()

# Save the figure
fig.savefig(r"C:\Users\Admin\Documents\SCHOOL\rc-charging-poc1\figures\generated\rc_tolerance.pdf")