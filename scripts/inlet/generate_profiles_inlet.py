import numpy as np
from scripts.inlet.velocity_inlet_functions import time_evolution_inlet
from scripts.common.files import write_points_file
from scripts.common.utils import clear_directory
from scripts.common.orr_sommerfeld_solution import parameters,solve_os_equation
from scripts.common.mesh import get_mesh_y_positions
import matplotlib.pyplot as plt
import os






def generate(dict, path, cell_centres):
    # --- File ---
    folder_path = os.path.join(path, "constant//velocityProfiles")
    constant_path = os.path.join(path, "constant")


    print("Clearing directory...")
    clear_directory(folder_path)
    print("Clearing directory... Done")

    print("Generating parameter values from .parameters file...")
    ny, nx, nz, yp, zp, alp2d, alp3d, beta, A2d, A3d, Re_b, n3d, n2d, Np, t, xp, Ucl, H = parameters(dict)
    Re_lam = 1.5*Re_b
    N = 100
    degree = 15

    # Get y position of the cell centres from the mesh
    y_cell_centres = get_mesh_y_positions(cell_centres, nx, ny)


    # Velocity profile
    print("Solving velocity profile")
    (
        yp_orr,
        u2d,
        v2d,
        w2d,
        u3dp,
        v3dp,
        w3dp,
        u3dm,
        v3dm,
        w3dm,
        om2d,
        om3dp,
        om3dm,
    ) = solve_os_equation(
        N,
        alp2d,
        alp3d,
        beta,
        Re_lam,
        n3d,
        n2d,
        Np
    )



    if not os.path.exists(path):
        os.makedirs(path)

    # Write velocity profiles
    write_inlet_velocity_profile_file(u2d, v2d, w2d, folder_path, "u2d", "imag")
    write_inlet_velocity_profile_file(u3dp, v3dp, w3dp, folder_path, "u3dp", "imag")
    write_inlet_velocity_profile_file(u3dm, v3dm, w3dm, folder_path, "u3dm", "imag")
    write_inlet_velocity_profile_file(u2d, v2d, w2d, folder_path, "u2d", "real")
    write_inlet_velocity_profile_file(u3dp, v3dp, w3dp, folder_path, "u3dp", "real")
    write_inlet_velocity_profile_file(u3dm, v3dm, w3dm, folder_path, "u3dm", "real")



    # Polynomial regresions
    u_list = [u2d, u3dp, v2d, v3dp, w2d, w3dp]
    y = np.linspace(0,H,N-1)

    # List of data
    coeffs = []

    names = ["u2d", "u2di", "u3d", "u3di", "v2d", "v2di", "v3d", "v3di", "w2d", "w2di", "w3d", "w3di"]

    # Fit profiles to curves
    for u in u_list:
        coeffs.append(np.flip(np.polyfit(y,np.real(u), degree)))
        coeffs.append(np.flip(np.polyfit(y,np.imag(u), degree)))

    # Write data to file
    write_polynomials_list(names, coeffs, constant_path)

    # n = 3
    # plt.plot(y,np.polyval(coeffs[2*n],y))
    # plt.plot(y, u_list[n])
    # plt.show()






def write_inlet_velocity_profile_file(u, v, w, folder_path, name, type):

    if type == "imag":
        data = np.column_stack((np.imag(u), np.imag(v), np.imag(w)))
        file_path = os.path.join(folder_path, name+"i")
    else:
        data = np.column_stack((np.real(u), np.real(v), np.real(w)))
        file_path = os.path.join(folder_path, name+"r")


    with open(file_path, 'w') as f:
        f.write('(\n')
        for row in data:
            f.write(f"({row[0]} {row[1]} {row[2]})\n")
        f.write(')\n')


def write_polynomials_list(names, coeff_list, constant_path):
    file_path = os.path.join(constant_path, "polynomialRegressions")
    print(f"Regressions path is {file_path}")
    with open(file_path, 'w') as f:
        # f.write('/*--------------------------------*- C++ -*----------------------------------*\n| =========                 |                                                 |\n| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n|  \\    /   O peration     | Version:  1.6                                   |\n|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n|    \\/     M anipulation  |                                                 |\n\*---------------------------------------------------------------------------*/\nFoamFile\n{\nversion     2.0;\nformat      ascii;\nclass       dictionary;\nlocation    "constant";\nobject      polynomialRegressionCoefficients;\n}\n// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n')


        for name, coeffs in zip(names, coeff_list):

            coeff_string = ""
            for coeff in coeffs:
                coeff_string = coeff_string + f" {coeff}"
            f.write(f"{coeff_string}\n")



