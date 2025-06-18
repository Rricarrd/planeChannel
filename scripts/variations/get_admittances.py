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
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
   
    ax1.set_xlabel("Lenght [m]")
    ax1.set_ylabel("Velocity [m/s]")
    ax2.set_xlabel("Lenght [m]")
    ax2.set_ylabel("Pressure [Pa]")
    


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

    # Get the full path of the current working directory
    current_working_directory = os.getcwd()

    # Extract just the last part (the directory name)
    directory_name = os.path.basename(current_working_directory)
            

    ax1.set_title(f"Velocity at bottom center line for time {float(last_time):.2f}")
    ax2.set_title(f"Pressure at bottom center line for time {float(last_time):.2f}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"../ret_plots/admittances_{directory_name}.eps")
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
    

        



    
    



