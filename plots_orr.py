import numpy as np
import os

from scripts.common.orr_sommerfeld_solution import (
    solve_os_equation,
    solve_os_equation_freqs_lambdas,
)

import matplotlib.pyplot as plt

# Enable LaTeX rendering
plt.rcParams["font.family"] = "serif"

# Create plots directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Define parameters
Re = 5000  # Reynolds number
N = 100  # Number of grid points
alp2d = 1.12  # Streamwise wavenumber
alp3d = 1.12  # Streamwise wavenumber for 3D case
beta = 2.1  # Perpendicular wavenumber
n3d = 2  # Number of modes in the 3D case
n2d = 0  # Number of modes in the 2D case
Np = 0

# Call functions
y2d, u2d, v2d, w2d, u3dp, v3dp, w3dp, u3dm, v3dm, w3dm, om2d, om3dp, om3dm = (
    solve_os_equation(
        N,
        alp2d,
        alp3d,
        beta,
        Re,
        n3d,
        n2d,
        Np,
    )
)

# Rainbow colors
colors = ["red", "orange", "green"]

# Plot u velocity profile
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(u2d.real, y2d, color=colors[0], label="2D mode", linewidth=2)
ax.plot(
    u3dp.real, y2d, color=colors[1], linestyle="--", label="3D mode (+)", linewidth=2
)
ax.plot(
    u3dm.real, y2d, color=colors[2], linestyle=":", label="3D mode (-)", linewidth=2
)
ax.set_xlabel(r"$u$ [m/s]")
ax.set_ylabel(r"$y$ [m]")
ax.set_title(r"Streamwise velocity profile $\mathbf{\vec{\hat{u}}}_{r_{2d}}(y)$")
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("plots/u_velocity_profile.eps", format='eps', bbox_inches='tight')
plt.show()

# Plot v velocity profile
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(v2d.real, y2d, color=colors[0], label="2D mode", linewidth=2)
ax.plot(
    v3dp.real, y2d, color=colors[1], linestyle="--", label="3D mode (+)", linewidth=2
)
ax.plot(
    v3dm.real, y2d, color=colors[2], linestyle=":", label="3D mode (-)", linewidth=2
)
ax.set_xlabel(r"$v$ [m/s]")
ax.set_ylabel(r"$y$ [m]")
ax.set_title(r"Wall-normal velocity profile $\mathbf{\vec{\hat{v}}}_{r_{2d}}(y)$")
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("plots/v_velocity_profile.eps", format='eps', bbox_inches='tight')
plt.show()

# Plot w velocity profile
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(w2d.real, y2d, color=colors[0], label="2D mode", linewidth=2)
ax.plot(
    w3dp.real, y2d, color=colors[1], linestyle="--", label="3D mode (+)", linewidth=2
)
ax.plot(
    w3dm.real, y2d, color=colors[2], linestyle=":", label="3D mode (-)", linewidth=2
)
ax.set_xlabel(r"$w$ [m/s]")
ax.set_ylabel(r"$y$ [m]")
ax.set_title(r"Spanwise velocity profile $\mathbf{\vec{\hat{w}}}_{r_{2d}}(y)$")
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.savefig("plots/w_velocity_profile.eps", format='eps', bbox_inches='tight')
plt.show()

# Get eigenvalues for the next plot
lam2d, lam3dp, lam3dm, om2d, om3dp, om3dm = solve_os_equation_freqs_lambdas(
    N,
    alp2d,
    alp3d,
    beta,
    Re,
    n3d,
    n2d,
    Np
)

# Plot 2D mode eigenvalues
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(lam2d.real, lam2d.imag, color=colors[0], s=50, alpha=0.7)
ax.set_xlabel(r"$\text{Re}(\lambda)$")
ax.set_ylabel(r"$\text{Im}(\lambda)$")
ax.set_title(r"2D Mode Eigenvalues")
ax.grid(True)
ax.set_ylim(-1, 0.2)
max_im_2d = np.max(lam2d.imag)
ax.axhline(max_im_2d, color="black", linestyle="--", label=rf"Most unstable mode$\to \text{{Im}}(\lambda) = {max_im_2d:.4f}$")
ax.legend()
plt.tight_layout()
plt.savefig("plots/eigenvalues_2d.eps", format='eps', bbox_inches='tight')
plt.show()

# Plot 3D mode (+) eigenvalues
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(lam3dp.real, lam3dp.imag, color=colors[1], s=50, alpha=0.7)
ax.set_xlabel(r"$\text{Re}(\lambda)$")
ax.set_ylabel(r"$\text{Im}(\lambda)$")
ax.set_title(r"3D Mode (+) Eigenvalues")
ax.grid(True)
ax.set_ylim(-1, 0.2)
max_im_3dp = np.max(lam3dp.imag)
ax.axhline(max_im_3dp, color="black", linestyle="--", label=rf"Most unstable mode$\to \text{{Im}}(\lambda) = {max_im_3dp:.4f}$")
ax.legend()
plt.tight_layout()
plt.savefig("plots/eigenvalues_3d_plus.eps", format='eps', bbox_inches='tight')
plt.show()

# Plot 3D mode (-) eigenvalues
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(lam3dm.real, lam3dm.imag, color=colors[2], s=50, alpha=0.7)
ax.set_xlabel(r"$\text{Re}(\lambda)$")
ax.set_ylabel(r"$\text{Im}(\lambda)$")
ax.set_title(r"3D Mode (-) Eigenvalues")
ax.grid(True)
ax.set_ylim(-1, 0.2)
max_im_3dm = np.max(lam3dm.imag)
ax.axhline(max_im_3dm, color="black", linestyle="--", label=rf"Most unstable mode$\to \text{{Im}}(\lambda) = {max_im_3dm:.4f}$")
ax.legend()
plt.tight_layout()
plt.savefig("plots/eigenvalues_3d_minus.eps", format='eps', bbox_inches='tight')
plt.show()
