import math
import pandas as pd

# ----------------- CURRENT PARAMETERS -----------------
# Fluid parameters
rho = 1
Re_lam = 5000
nu = 1/Re_lam

# Channel parameters
H = 2                       # Channel height (Characteristic length) [m]
h = H/2                  # Channel total height [m]
W = 2*math.pi/2.1           # Channel width [m]
L = 2*math.pi/1.12          # Channel length [m]

# Iteration parameters
R_values = [8, 12, 16, 24, 24, 24]
n_values = [16, 24, 32, 48, 64, 96]

# Storage for results
results = []

print("######################### MESH CALCULATIONS #######################\n")

# ----------------- DESIRED MESH SIZING -----------------
print("############ Calculations of the desired mesh ############\n")

# y with Re and y+
print("# Imposing Re and U")
yplus = 1
U = 1
Ub = 2/3
print(f"Considering yplus is {yplus} and U is {U:.3f} m/s")

# 1 - Reynolds number
Reb = Ub * h / nu
print(f"The bulk Reynolds number (Re) is {Reb:.3f}")

# 2 - Friction coefficient
Cf = 0.058 * (Reb ** (-0.2))

# 3 - Shear stress
tauw = 0.5 * Cf * rho * (U ** 2)

# 4 - Shear speed
Ut = math.sqrt(tauw / rho)

# 5 - y first cell
yReb = nu * yplus / Ut
print(f"Yielding a first cell height of {yReb:.3f} m or {yReb * 1000:.3f} mm\n")

# y with Ret
print("# Imposing shear Reynolds (Ret)")
Ret = 208
print(f"Considering Ret is {Ret}")

# 1 - Ut calculation using Ret
Ut = Ret * nu / h

# 2 - y first cell
yRet = nu * yplus / Ut
print(f"Yielding a first cell height of {yRet:.3f} m or {yRet * 1000:.3f} mm\n")

def final_element_size(L, r, N):
      """
      Calculate the smallest cell size at the wall using the geometric progression formula.
      """
      return L * (r - 1) * (r ** (N - 1)) / (r ** N - 1)

# ----------------- ITERATE THROUGH R AND N VALUES -----------------
print("############ Iterating through R and n values ############\n")

for i, (R_val, n_val) in enumerate(zip(R_values, n_values)):
      print(f"--- Iteration {i+1}: R = {R_val}, n = {n_val} ---")
      
      # Use the same R and n values for all directions
      Rx = 1 + 1e-12
      Ry = R_val
      Rz = 1 + 1e-12
      nx = n_val
      ny = n_val
      nz = n_val
      
      # Geometric progression factors
      rx = Rx ** (-1 / (nx/2 - 1))
      ry = Ry ** (-1 / (ny/2 - 1))
      rz = Rz ** (-1 / (nz/2 - 1))
      
      # Cell sizes [m] (for x and z, since R=1, all cells are the same size)
      cell_dx = L / nx
      mincell_dy = final_element_size(H/2, ry, ny/2)
      cell_dz = W / nz
      
      # Biggest cell size for y direction [m]
      maxcell_dy = Ry * mincell_dy
      
      # Calculate dimensionless values
      mincell_yplus = mincell_dy * Ut / nu
      maxcell_yplus = maxcell_dy * Ut / nu
      xplus = cell_dx * Ut / nu
      zplus = cell_dz * Ut / nu
      
      print(f"  Cell dx = {cell_dx * 1000:.3f} mm, x+ = {xplus:.3f}")
      print(f"  Min cell dy = {mincell_dy * 1000:.3f} mm, y+ = {mincell_yplus:.3f}")
      print(f"  Max cell dy = {maxcell_dy * 1000:.3f} mm, y+ = {maxcell_yplus:.3f}")
      print(f"  Cell dz = {cell_dz * 1000:.3f} mm, z+ = {zplus:.3f}")
      
      # Store results
      results.append({
            'R': R_val,
            'n': n_val,
            'nx': nx,
            'ny': ny,
            'nz': nz,
            'dx_mm': cell_dx * 1000,
            'min_dy_mm': mincell_dy * 1000,
            'max_dy_mm': maxcell_dy * 1000,
            'dz_mm': cell_dz * 1000,
            'xplus': xplus,
            'min_yplus': mincell_yplus,
            'max_yplus': maxcell_yplus,
            'zplus': zplus
      })
      print()

# ----------------- SAVE RESULTS -----------------
print("############ Final Results Summary ############")
df = pd.DataFrame(results)
print(df.to_string(index=False, float_format='%.3f'))

# Save to CSV
df.to_csv('mesh_results.csv', index=False, float_format='%.3f')
print(f"\nResults saved to 'mesh_results.csv'")

# Print summary
print("\n############ Cell Size and Dimensionless Values Summary ############")
for i, result in enumerate(results):
      print(f"R={result['R']}, n={result['n']}: x+ = {result['xplus']:.3f}, min_y+ = {result['min_yplus']:.3f}, max_y+ = {result['max_yplus']:.3f}, z+ = {result['zplus']:.3f}")
      print(f"  dx: {result['dx_mm']:.3f} mm")
      print(f"  dy: {result['min_dy_mm']:.3f}-{result['max_dy_mm']:.3f} mm") 
      print(f"  dz: {result['dz_mm']:.3f} mm")
      print()
