import numpy as np
import os


def get_points(yp, zp):

    xpoints = np.zeros((len(yp), len(zp)), dtype=float)
    ypoints = np.zeros((len(yp), len(zp)), dtype=float)
    zpoints = np.zeros((len(yp), len(zp)), dtype=float)

    for i, y in enumerate(yp):
        for j, z in enumerate(zp):
            ypoints[j, i] = y
            zpoints[j, i] = z

    xpoints = xpoints.flatten()
    ypoints = ypoints.flatten()
    zpoints = zpoints.flatten()
    
    points = np.column_stack((xpoints, ypoints, zpoints))

    return points

def write_points_file(yp,zp,folder_path):
    points = get_points(yp, zp)
    file_path_p = os.path.join(folder_path, f"points")
    with open(file_path_p, 'w') as f:
        f.write('(\n')
        for row in points:
            f.write(f"({row[0]} {row[1]} {row[2]})\n")
        f.write(')\n')




