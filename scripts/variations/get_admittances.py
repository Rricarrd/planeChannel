import os
import pickle
import matplotlib.pyplot as plt
import json
import openfoamparser as Ofpp
import numpy as np
import re
import sys
import scipy
from scipy.signal import lombscargle



def extract_number(name):
    num = ""
    for char in name:
        if char.isdigit():
            num += char
        else:
            break
    return int(num) if num else 0



def plot_admitance_time(folders, current_directory):

    print("Plotting pressure and velocity at the wall")
    # Create a simple matplotlib figure
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))
   
    ax1.set_xlabel("Lenght [m]")
    ax1.set_ylabel("Velocity [m/s]")
    ax2.set_xlabel("Lenght [m]")
    ax2.set_ylabel("Pressure [Pa]")
    ax3.set_xlabel("Lenght [m]")
    ax3.set_ylabel("Phase correlation")
    


    # Iterate through each folder and check for the pickled file
    for folder in folders:  
        if folder[0].isdigit():
            try:

                # Construct the full path to the folder
                folder_path = os.path.join(current_directory, folder)


                # Parse the foam file
                print("Folder path is: ", folder_path)
                parameters_path = os.path.join(folder_path, "default.parameters")
                parsed_data = parse_foam_file(parameters_path)

                print(f"Checking folder: {folder}. Folder path is: {folder_path}")
                times = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
                times.sort(key=extract_number)

                last_time = times[-1]
                last_time_path = os.path.join(folder_path, last_time)

                print(f"Checking last time: {last_time}")
                U_last=Ofpp.parse_internal_field(f'{str(folder_path)}/{str(last_time)}/U')
                p_last=Ofpp.parse_internal_field(f'{str(folder_path)}/{str(last_time)}/p')
                C=Ofpp.parse_internal_field(f'{str(folder_path)}/constant/C')

                mesh = Ofpp.FoamMesh(f'{folder}')
                wall_cell_indices = np.array(list(mesh.boundary_cells(b'bottom')))
                
                
                # Get pressure at wall cells
                wall_pressures = []
                wall_velocities = []
                wall_coordinates = []
                
                
                for cell_idx in wall_cell_indices:
                    # Get values at the wall cells
                    wall_pressures.append(p_last[cell_idx])
                    wall_velocities.append(U_last[cell_idx][1])
                    wall_coordinates.append(C[cell_idx])
                    


                # Convert to numpy arrays for easier processing
                wall_pressures = np.array(wall_pressures)
                wall_velocities = np.array(wall_velocities)
                wall_coordinates = np.array(wall_coordinates)
                
                # Extract x, y, z coordinates
                nz = parsed_data["nz"]
                
                # Find the middle position (nz/2)
                mid_pos = nz // 2

                # Select every nz elements from pressure and velocity arrays starting from mid_pos
                selected_pressures = wall_pressures[mid_pos::nz]
                selected_velocities = wall_velocities[mid_pos::nz]
                selected_coordinates = wall_coordinates[mid_pos::nz]
                
                # Fit selected pressures and velocities to sine waves
                x_coords = selected_coordinates[:, 0]
                
                # Define sine wave function: A * sin(2*pi*x/L + phi) + offset
                def sine_wave(x, amplitude, wavelength, phase, offset):
                    return amplitude * np.sin(2 * np.pi * x / wavelength + phase) + offset
                
                # Initial guess for parameters [amplitude, wavelength, phase, offset]
                # Use domain length as initial wavelength guess
                domain_length = x_coords[-1] - x_coords[0]
                
                # Fit pressure data
                p_initial_guess = [np.std(selected_pressures), domain_length, 0, np.mean(selected_pressures)]
                try:
                    p_params, _ = scipy.optimize.curve_fit(sine_wave, x_coords, selected_pressures, p0=p_initial_guess)
                    pressure_amplitude = abs(p_params[0])
                except:
                    pressure_amplitude = np.std(selected_pressures)
                    print(f"Warning: Could not fit pressure sine wave for {folder}")
                
                # Fit velocity data
                v_initial_guess = [np.std(selected_velocities), domain_length, 0, np.mean(selected_velocities)]
                try:
                    v_params, _ = scipy.optimize.curve_fit(sine_wave, x_coords, selected_velocities, p0=v_initial_guess)
                    velocity_amplitude = abs(v_params[0])
                except:
                    velocity_amplitude = np.std(selected_velocities)
                    print(f"Warning: Could not fit velocity sine wave for {folder}")
                
                print(f"Pressure amplitude: {pressure_amplitude:.6f} Pa")
                print(f"Velocity amplitude: {velocity_amplitude:.6f} m/s")

                # Calculate admittance (velocity/pressure ratio)
                admittance = velocity_amplitude / pressure_amplitude
                
                print(f"Admittance: {admittance:.6f} m/sPa")
                

                # Use the arctan2 function to calculate the phase angle for complex data
                phase_diff_corr = scipy.signal.signaltools.correlate(selected_velocities, selected_pressures)
                
                dx = np.linspace(-selected_coordinates[:, 0][-1], selected_coordinates[:, 0][-1], 2*nz-1)
                recovered_space_shift = dx[phase_diff_corr.argmax()]
                
                # Calculate wavelength (assuming the domain length is the wavelength)
                wavelength = selected_coordinates[:, 0][-1] - selected_coordinates[:, 0][0]

                # Calculate phase difference in radians (2π * spatial_shift / wavelength)
                phase_diff_rad = 2 * np.pi * (recovered_space_shift / wavelength)

                # Convert to degrees
                phase_diff_deg = np.degrees(phase_diff_rad)

                # Store the phase difference for reporting
                phase_diff = f"{phase_diff_rad:.4f} rad ({phase_diff_deg:.2f}°)"

                print(f"Space shift: {recovered_space_shift:.6f} m")
                print(f"Phase difference: {phase_diff}")
                
                
                # Plot admittance vs x-coordinate
                ax1.plot(selected_coordinates[:, 0], selected_velocities, label=f"{folder}")
                ax2.plot(selected_coordinates[:, 0], selected_pressures, label=f"{folder}")
                

                
                

  



            except KeyError as e:
                print(f"KeyError: {e} in folder: {folder}")

    # Reference data DNS
    # times_dns = [9.79765708200213, 25.559105431309906, 42.17252396166134, 57.082002129925456, 69.43556975505858, 82.64110756123536, 95.42066027689032, 107.77422790202344, 117.14589989350374, 126.0915867944622, 132.48136315228967, 138.0191693290735, 142.2790202342918, 145.26091586794462, 147.3908413205538, 150.3727369542066, 152.50266240681577, 155.05857294994675, 158.0404685835996, 160.17039403620873, 162.72630457933974, 165.28221512247072, 167.83812566560172, 170.3940362087327, 172.09797657082004, 175.07987220447285, 178.06176783812566, 180.19169329073483, 183.17358892438764, 188.71139510117146, 193.82321618743345, 197.2310969116081, 201.0649627263046, 201.49094781682643, 207.02875399361022, 210.86261980830673, 217.2523961661342, 223.21618743343984, 227.47603833865816, 233.86581469648564, 237.69968051118212, 241.10756123535677, 247.07135250266242, 256.8690095846645, 261.98083067092654, 266.6666666666667, 272.2044728434505, 276.038338658147, 282.8541001064963, 289.66986155484557, 294.7816826411076, 299.89350372736953, 309.26517571884983, 316.93290734824285, 330.1384451544196, 335.67625133120345, 341.21405750798726, 345.8998935037274, 351.86368477103304, 361.66134185303514, 374.0149094781683, 380.8306709265176, 382.96059637912674, 386.7944621938232, 390.6283280085197, 397.44408945686905]
    # ret_dns = [101.14503816793894, 101.6030534351145, 101.6030534351145, 101.37404580152672, 101.37404580152672, 101.14503816793894, 101.37404580152672, 102.29007633587786, 104.12213740458016, 107.32824427480917, 112.13740458015268, 117.17557251908397, 121.98473282442748, 128.62595419847327, 133.89312977099237, 140.53435114503816, 149.9236641221374, 160.2290076335878, 179.92366412213738, 194.35114503816794, 205.34351145038167, 219.08396946564886, 227.09923664122135, 236.2595419847328, 242.90076335877862, 244.50381679389312, 242.67175572519085, 238.54961832061068, 233.2824427480916, 223.66412213740458, 221.83206106870227, 218.62595419847327, 213.3587786259542, 209.6946564885496, 209.46564885496184, 208.0916030534351, 203.51145038167937, 201.6793893129771, 201.22137404580153, 202.59541984732823, 204.42748091603053, 204.8854961832061, 204.19847328244276, 206.4885496183206, 205.34351145038167, 204.19847328244276, 204.6564885496183, 207.17557251908397, 207.63358778625954, 207.17557251908397, 206.71755725190837, 207.40458015267177, 209.23664122137404, 210.61068702290078, 210.83969465648855, 211.5267175572519, 213.81679389312978, 211.5267175572519, 210.61068702290078, 207.63358778625954, 207.8625954198473, 208.0916030534351, 209.00763358778624, 210.61068702290078, 211.29770992366412, 212.44274809160305]

    #ax.scatter(times_dns, ret_dns, label="DNS")
            

    ax1.set_title(f"Velocity at bottom center line for time {last_time}")
    ax2.set_title(f"Pressure at bottom center line for time {last_time}")
    plt.legend()
    plt.savefig("velo_press.png")
    plt.show()




def parse_foam_file(filepath):

    """
    Parses a Foam-like file into a Python dictionary.
    Args:
        filepath (str): The path to the file.
        
    Returns:
        dict: A dictionary containing the parsed data, or None if an error occurs.
    """

    try:

        data = {}

        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                
                if line and not line.startswith('//'):  # Skip empty lines and comments
                    parts = line.split(';')
                    
                    if len(parts) > 1:
                        key_value = parts[0].strip().split()
                        
                        if len(key_value) == 2:
                            key, value = key_value
                            value = value.strip()
                            
                            try:
                                # Attempt to convert to appropriate data types

                                if '.' in value or 'e' in value:
                                    value = float(value)

                                elif value.lower() == 'true':
                                    value = True

                                elif value.lower() == 'false':
                                    value = False

                                else:
                                    value = int(value)

                            except ValueError:
                                # If conversion fails, keep it as a string
                                pass

                            data[key] = value

        return data

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None




def get_x_values_according_to_folder(folder):
    """
    Extracts the x values from the folder name.
    """
    x_type = ""
    value_flag = True
    x_values = []

    # Split by underscore
    parts = folder.split('_')
    print(f"Parts: {parts}")
    
    if len(parts) >= 3:
        # Second element is the value, third element is the type
        value = parts[1]
        folder_type = parts[2]
        
        print(f"Extracting value and type from folder: {folder}")
        print(f"Value: {value}, Type: {folder_type}")
        
        # Try to convert value to float if possible
        try:
            value = float(value)
        except:
            value = value.strip()
            value_flag = False
        
        # Determine the x values based on the folder type
        if folder_type == "nx":
            x_type = "Mesh size"
        elif folder_type == "amplitude":
            x_type = "Transpiration BC Amplitude"
        elif folder_type == "maxCo":
            x_type = "Max Courant number"
        elif folder_type == "model":
            x_type = "Turbulence Model"
        elif folder_type == "schemes":
            x_type = "Numerical Schemes"
        else:
            x_type = "Unknown"

    return value_flag, value, x_type



if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()

    # List all folders in the current directory
    folders = [name for name in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, name))]
    folders.sort(key=extract_number)

    # Print the folder names
    print(f"Checked cases are {folders}")

    # Plots dictionary
    pickled_plots_names = {
        'InOut': '1',
        'Residuals': '2',
        'Residuals': '3',
        'Global': '4',
        'Residuals': '5',
        'Global': '6',
        'Courant': '7',
        'ReTau': '8',
    }

    # # Check for arguments
    # if len(sys.argv) != 2 or sys.argv[1].lower() not in ["time", "space","skip","fast"]:
    #     print("Usage: python plot_all.py [time|space|skip|fast]")
    #     sys.exit(1)

    plot_admitance_time(folders, current_directory)
    

        



    
    



