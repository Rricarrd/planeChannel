import os
import pickle
import matplotlib.pyplot as plt
import json
import openfoamparser as Ofpp
import numpy as np
import re
import sys
from scipy.signal import lombscargle


def extract_number(name):
    num = ""
    for char in name:
        if char.isdigit():
            num += char
        else:
            break
    return int(num) if num else 0



def plot_retau_time(folders, current_directory, plots_names, skip=False):
    print("Printing Retau time")

    # Start maximum Retau point list
    max_retau_time = []
    turbulent_retau_avg = []

    # Create a simple matplotlib figure
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_title(r"Channel $Re_{\tau}$ over time")
    ax.set_xlabel("t [s]")
    ax.set_ylabel(r"$Re_{\tau}$ ")
    ax.set_xlim(0, 450)
    ax.set_ylim(85, 290)
    

    # Iterate through each folder and check for the pickled file
    for folder in folders:
        pickled_file_path = os.path.join(current_directory, folder, "log.pimpleFoam.analyzed/pickledPlots")
        print(f"Checking folder: {folder}")
        print(f"Pickled file path: {pickled_file_path}")

        if folder[0].isdigit() and os.path.exists(pickled_file_path):
            try:
                with open(pickled_file_path, "rb") as file:
                    data = pickle.load(file)

                    # Extract Retau values and times
                    ret = data[plots_names['ReTau']]['values']['avg']
                    times = data[plots_names['ReTau']]['times']
                    
                    # Find the maximum Retau value and its corresponding time
                    max_retau_index = np.argmax(ret)
                    max_retau_value = ret[max_retau_index]
                    max_retau_time_value = times[max_retau_index]
                    print(f"Maximum Retau in {folder}: {max_retau_value:.2f} at time {max_retau_time_value:.2f}")

                    # Store the maximum retau and time for later use if needed
                    max_retau_time.append((folder, max_retau_value, max_retau_time_value))
                    

                    # Calculate the average Retau value after the maximum (only for times >= 300)
                    turbulent_indices = [i for i, t in enumerate(times) if t >= 300]
                    if turbulent_indices:
                        turbulent_ret = [ret[i] for i in turbulent_indices]
                        avg_retau_value = np.mean(turbulent_ret)
                        turbulent_retau_avg.append((folder, avg_retau_value))
                        print(f"Average turbulent Retau in {folder} (after t=300): {avg_retau_value:.2f}")
                    else:
                        avg_retau_value = np.mean(ret[max_retau_index:])
                        print(f"No data after t=300, using data after max Retau instead")
                        avg_retau_value = np.mean(ret[max_retau_index:])
                    
                    


                    # Format folder name to display as "name = value"
                    folder_name = re.sub(r'^\d+_', '', folder)
                    folder_name = folder_name.capitalize()

                    if '_' in folder_name and len(folder_name.split('_')) >= 2:
                        parts = folder_name.split('_')
                        formatted_name = f"{parts[1]} = {parts[0]}"
                    else:
                        formatted_name = folder_name
                        

                    ax.plot(times, ret, label=formatted_name)

                    

            except KeyError as e:
                print(f"KeyError: {e} in folder: {folder}")

    # Reference data DNS
    times_dns = [9.79765708200213, 25.559105431309906, 42.17252396166134, 57.082002129925456, 69.43556975505858, 82.64110756123536, 95.42066027689032, 107.77422790202344, 117.14589989350374, 126.0915867944622, 132.48136315228967, 138.0191693290735, 142.2790202342918, 145.26091586794462, 147.3908413205538, 150.3727369542066, 152.50266240681577, 155.05857294994675, 158.0404685835996, 160.17039403620873, 162.72630457933974, 165.28221512247072, 167.83812566560172, 170.3940362087327, 172.09797657082004, 175.07987220447285, 178.06176783812566, 180.19169329073483, 183.17358892438764, 188.71139510117146, 193.82321618743345, 197.2310969116081, 201.0649627263046, 201.49094781682643, 207.02875399361022, 210.86261980830673, 217.2523961661342, 223.21618743343984, 227.47603833865816, 233.86581469648564, 237.69968051118212, 241.10756123535677, 247.07135250266242, 256.8690095846645, 261.98083067092654, 266.6666666666667, 272.2044728434505, 276.038338658147, 282.8541001064963, 289.66986155484557, 294.7816826411076, 299.89350372736953, 309.26517571884983, 316.93290734824285, 330.1384451544196, 335.67625133120345, 341.21405750798726, 345.8998935037274, 351.86368477103304, 361.66134185303514, 374.0149094781683, 380.8306709265176, 382.96059637912674, 386.7944621938232, 390.6283280085197, 397.44408945686905]
    ret_dns = [101.14503816793894, 101.6030534351145, 101.6030534351145, 101.37404580152672, 101.37404580152672, 101.14503816793894, 101.37404580152672, 102.29007633587786, 104.12213740458016, 107.32824427480917, 112.13740458015268, 117.17557251908397, 121.98473282442748, 128.62595419847327, 133.89312977099237, 140.53435114503816, 149.9236641221374, 160.2290076335878, 179.92366412213738, 194.35114503816794, 205.34351145038167, 219.08396946564886, 227.09923664122135, 236.2595419847328, 242.90076335877862, 244.50381679389312, 242.67175572519085, 238.54961832061068, 233.2824427480916, 223.66412213740458, 221.83206106870227, 218.62595419847327, 213.3587786259542, 209.6946564885496, 209.46564885496184, 208.0916030534351, 203.51145038167937, 201.6793893129771, 201.22137404580153, 202.59541984732823, 204.42748091603053, 204.8854961832061, 204.19847328244276, 206.4885496183206, 205.34351145038167, 204.19847328244276, 204.6564885496183, 207.17557251908397, 207.63358778625954, 207.17557251908397, 206.71755725190837, 207.40458015267177, 209.23664122137404, 210.61068702290078, 210.83969465648855, 211.5267175572519, 213.81679389312978, 211.5267175572519, 210.61068702290078, 207.63358778625954, 207.8625954198473, 208.0916030534351, 209.00763358778624, 210.61068702290078, 211.29770992366412, 212.44274809160305]

    ax.scatter(times_dns, ret_dns, label="DNS")
    
    
    # Get the full path of the current working directory
    current_working_directory = os.getcwd()

    # Extract just the last part (the directory name)
    directory_name = os.path.basename(current_working_directory)
            
    plt.legend()
    plt.savefig(f"../ret_plots/variations_ret_time_{directory_name}.eps")
    
    if not skip:
        plt.show()
    
    return max_retau_time, turbulent_retau_avg

def plot_retau_space(folders, current_directory, skip=False):
    
    print("Printing Retau space")
    # Create a simple matplotlib figure
    fig, ax = plt.subplots()
    
    ax.set_xlabel("Lenght [m]")
    ax.set_ylabel("Ret")

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

                wss_time_path_string = f'{str(folder_path)}/{str(last_time)}/wallShearStressMean'
                wss=Ofpp.parse_boundary_field(wss_time_path_string)

                # Calculate the average wall shear stress per X coordinate
                mags_top = np.array(np.linalg.norm(wss[b"top"][b"value"],axis=1))
                mags_bot = np.array(np.linalg.norm(wss[b"bottom"][b"value"],axis=1))
                tau = 0.5*np.abs(np.add(mags_top,mags_bot))

                n = parsed_data["nz"]
                averaged_tau_values = [np.mean(tau[i:i+n]) for i in range(0, len(tau), n)]


                ut = np.sqrt(averaged_tau_values)
                ret = ut*(parsed_data["H"]/2)/parsed_data["nu"]
                x = np.linspace(0, parsed_data["L"], len(ret))
                
                # Format folder name to display as "name = value"
                folder_name = re.sub(r'^\d+_', '', folder)
                folder_name = folder_name.capitalize()
                if '_' in folder_name and len(folder_name.split('_')) >= 2:
                    parts = folder_name.split('_')
                    formatted_name = f"{parts[1]} = {parts[0]}"
                    
                else:
                    formatted_name = folder_name
                        
                
                ax.scatter(x,ret, label=formatted_name)


            except KeyError as e:
                print(f"KeyError: {e} in folder: {folder}")

    # Reference data DNS
    # times_dns = [9.79765708200213, 25.559105431309906, 42.17252396166134, 57.082002129925456, 69.43556975505858, 82.64110756123536, 95.42066027689032, 107.77422790202344, 117.14589989350374, 126.0915867944622, 132.48136315228967, 138.0191693290735, 142.2790202342918, 145.26091586794462, 147.3908413205538, 150.3727369542066, 152.50266240681577, 155.05857294994675, 158.0404685835996, 160.17039403620873, 162.72630457933974, 165.28221512247072, 167.83812566560172, 170.3940362087327, 172.09797657082004, 175.07987220447285, 178.06176783812566, 180.19169329073483, 183.17358892438764, 188.71139510117146, 193.82321618743345, 197.2310969116081, 201.0649627263046, 201.49094781682643, 207.02875399361022, 210.86261980830673, 217.2523961661342, 223.21618743343984, 227.47603833865816, 233.86581469648564, 237.69968051118212, 241.10756123535677, 247.07135250266242, 256.8690095846645, 261.98083067092654, 266.6666666666667, 272.2044728434505, 276.038338658147, 282.8541001064963, 289.66986155484557, 294.7816826411076, 299.89350372736953, 309.26517571884983, 316.93290734824285, 330.1384451544196, 335.67625133120345, 341.21405750798726, 345.8998935037274, 351.86368477103304, 361.66134185303514, 374.0149094781683, 380.8306709265176, 382.96059637912674, 386.7944621938232, 390.6283280085197, 397.44408945686905]
    # ret_dns = [101.14503816793894, 101.6030534351145, 101.6030534351145, 101.37404580152672, 101.37404580152672, 101.14503816793894, 101.37404580152672, 102.29007633587786, 104.12213740458016, 107.32824427480917, 112.13740458015268, 117.17557251908397, 121.98473282442748, 128.62595419847327, 133.89312977099237, 140.53435114503816, 149.9236641221374, 160.2290076335878, 179.92366412213738, 194.35114503816794, 205.34351145038167, 219.08396946564886, 227.09923664122135, 236.2595419847328, 242.90076335877862, 244.50381679389312, 242.67175572519085, 238.54961832061068, 233.2824427480916, 223.66412213740458, 221.83206106870227, 218.62595419847327, 213.3587786259542, 209.6946564885496, 209.46564885496184, 208.0916030534351, 203.51145038167937, 201.6793893129771, 201.22137404580153, 202.59541984732823, 204.42748091603053, 204.8854961832061, 204.19847328244276, 206.4885496183206, 205.34351145038167, 204.19847328244276, 204.6564885496183, 207.17557251908397, 207.63358778625954, 207.17557251908397, 206.71755725190837, 207.40458015267177, 209.23664122137404, 210.61068702290078, 210.83969465648855, 211.5267175572519, 213.81679389312978, 211.5267175572519, 210.61068702290078, 207.63358778625954, 207.8625954198473, 208.0916030534351, 209.00763358778624, 210.61068702290078, 211.29770992366412, 212.44274809160305]

    #ax.scatter(times_dns, ret_dns, label="DNS")
            

    # Get the full path of the current working directory
    current_working_directory = os.getcwd()

    # Extract just the last part (the directory name)
    directory_name = os.path.basename(current_working_directory)

    ax.set_title(f"Channel Ret over space at time {last_time}")

    plt.legend()
    plt.savefig(f"../ret_plots/variations_ret_space_{current_working_directory}.eps")
    if not skip:
        plt.show()

def plot_u_sample(folders, current_directory, skip=False):
    """
    Plot the U velocity component from probe data files across different cases.
    """
    print("Plotting U velocity from probe data")
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_title("U Velocity at Probe Location")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("U Velocity [m/s]")
    ax.set_xlim(0, 450)
    ax.grid(True)
    
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.set_title("Lomgb-Scargle Periodogram")
    ax2.set_xlabel("Frequency [rad/s]")
    ax2.set_ylabel("Power")
    ax.grid(True)
    
    for folder in folders:
        if folder[0].isdigit():
            try:
                # Construct the path to the probe file
                probe_file_path = os.path.join(current_directory, folder, "postProcessing/samplingUPoints/0/U")
                
                if os.path.exists(probe_file_path):
                    # Read and parse the probe data
                    times = []
                    u_values = []
                    
                    with open(probe_file_path, 'r') as file:
                        # Skip header lines
                        for i in range(3):
                            next(file)
                        
                        # Process data lines
                        for line in file:
                            line = line.strip()
                            if line and not line.startswith('#'):
                                parts = line.split()
                                if len(parts) >= 4:
                                    time = float(parts[0])
                                    # Extract U component (first value in the vector)
                                    u_value = float(parts[1].strip('('))
                                    
                                    times.append(time)
                                    u_values.append(u_value)
                    
                    
                    # Format folder name to display as "name = value"
                    folder_name = re.sub(r'^\d+_', '', folder)
                    folder_name = folder_name.capitalize()
                    if '_' in folder_name and len(folder_name.split('_')) >= 2:
                        parts = folder_name.split('_')
                        formatted_name = f"{parts[1]} = {parts[0]}"
                    else:
                        formatted_name = folder_name
                        
                    # Plot the data    
                    ax.plot(times, u_values, label=formatted_name)
                    print(f"Plotting U velocity for folder: {folder_name}")
                    
                    # Process power spectrum with Lomgb-Scargle Periodogram
                    # Select data after t=300
                    mask = np.array(times) >= 300
                    times_filtered = np.array(times)[mask]
                    u_values_filtered = np.array(u_values)[mask]

                    # Only process if we have enough data points
                    if len(times_filtered) > 10:
                        # Use filtered data for spectrum analysis
                        u_values_detrended = u_values_filtered - np.mean(u_values_filtered)
                        
                        omega = np.linspace(0.0001, 100, 500)*2*np.pi  # Adjust frequency range as needed
                        pgram = lombscargle(times_filtered, u_values_filtered, omega)
                        ax2.loglog(omega, pgram, label=formatted_name)
                        print(f"Plotting Lomb-Scargle periodogram for folder: {folder_name}")
                    
            except Exception as e:
                print(f"Error processing folder {folder}: {e}")
    
    
    # Add a reference line with -5/3 slope for Kolmogorov's law
    # Use a wide frequency range to show the theoretical slope
    ref_freqs = np.logspace(-3, 4, 1000)
    ref_power = ref_freqs**(-5/3)
    
    # Scale the reference line to fit in the plot
    scale_factor = 1.0
    if len(ax2.get_lines()) > 0:
        # Get the maximum power value from the existing plots to scale the reference line
        max_power = max([np.max(line.get_ydata()) for line in ax2.get_lines()])
        scale_factor = max_power / np.max(ref_power) * 0.5  # Scale to make it visible
    
    ax2.loglog(ref_freqs, ref_power * scale_factor, 'k--', label=r'$\omega^{-5/3}$ (Kolmogorov)')
    
    
    # Get the full path of the current working directory
    current_working_directory = os.getcwd()

    # Extract just the last part (the directory name)
    directory_name = os.path.basename(current_working_directory)
    
    # Add labels to ax2
    ax2.legend()
    ax2.grid(True)
    plt.tight_layout()
    plt.savefig(f"../ret_plots/variations_spectrum_{directory_name}.eps")
    
    plt.legend()
    plt.grid(True)
    plt.savefig(f"../ret_plots/variations_u_velocity_{directory_name}.eps")

    if not skip:
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

# Save the max_retau_time and turbulent_retau_avg to a JSON file
def save_retau_data(max_retau_time, turbulent_retau_avg):
    # Convert the data to a more JSON-friendly format
    max_retau_data = [{"folder": folder, "max_retau": float(max_val), "time": float(time_val)} 
                        for folder, max_val, time_val in max_retau_time]
    
    turbulent_data = [{"folder": folder, "avg_retau": float(avg_val)} 
                        for folder, avg_val in turbulent_retau_avg]
    
    # Create a dictionary to store both datasets
    data_to_save = {
        "max_retau_time": max_retau_data,
        "turbulent_retau_avg": turbulent_data
    }
    
    # Save to a JSON file
    with open("retau_data.json", "w") as f:
        json.dump(data_to_save, f, indent=4)
    
    print("Saved ReTau data to retau_data.json")


def plot_retau_summary(max_retau_times, turbulent_retau_avgs, skip=False):
    """
    Plot summary of max ReTau times and average ReTau values against folder names.
    
    Args:
        max_retau_time: List of tuples (folder, max_retau, time)
        turbulent_retau_avg: List of tuples (folder, avg_retau)
    """
    print("Plotting ReTau summary")
    
    # Create figure with two subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 7))
    
    folders = []
    max_values = []
    max_times = []
    avg_values = []
    x_values_max = []
    x_values_avg = []
    
    for max_retau_time, turbulent_retau_avg in zip(max_retau_times, turbulent_retau_avgs):
        
        # Get values and times
        folder = max_retau_time[0]
        folders.append(folder)
        max_values.append(max_retau_time[1])
        max_times.append(max_retau_time[2])
        avg_values.append(turbulent_retau_avg[1])
        

        # Generate x values max
        value_flag_max, x_value_max, x_type_max = get_x_values_according_to_folder(max_retau_time[0])
        x_values_max.append(x_value_max)
        
        # Generate x values avg
        value_flag_avg, x_value_avg, x_type_avg = get_x_values_according_to_folder(turbulent_retau_avg[0])
        x_values_avg.append(x_value_avg)
        

    # Plot maximum ReTau values
    if value_flag_max:
        ax1.plot(x_values_max, max_values, label="Max ReTau", color='blue')
        ax1.set_xlabel(x_type_max)
        ax1.set_ylabel(r'Max $Re_{\tau}$')
        ax1.set_title(r"Maximum $Re_{\tau}$ Values")
        ax1.set_xticks(x_values_max)
        ax1.grid(True, alpha=0.7)
    else:
        bars1 = ax1.plot(folders_max, max_values)
        ax1.set_title(r"Maximum $Re_{\tau}$ u Values")
        ax1.set_xlabel(x_type_max)
        ax1.set_ylabel(r"Max $Re_{\tau}$")
        ax1.set_title(r"Maximum $Re_{\tau}$ Values")
        ax1.set_xticklabels(folder, rotation=45, ha='right')
        ax1.grid(axis='y', linestyle='--', alpha=0.7)
        
    # Plot maximum ReTau times
    if value_flag_max:
        ax2.plot(x_values_max, max_times, label="Max Times", color='red')
        ax2.set_xlabel(x_type_max)
        ax2.set_ylabel(r"Time for max $Re_{\tau}$ [s]")
        ax2.set_title(r"Maximum $Re_{\tau}$ Times")
        ax2.set_xticks(x_values_max)
        ax2.grid(True, alpha=0.7)
        
    else:
        bars2 = ax2.plot(folders_max, max_times)
        ax2.set_title(r"Maximum $Re_{\tau}$ Values")
        ax2.set_xlabel(x_type_max)
        ax2.set_ylabel(r"Time for max $Re_{\tau}$")
        ax2.set_title(r"Maximum $Re_{\tau}$ Values")
        ax2.set_xticklabels(folders, rotation=45, ha='right')
        ax2.grid(axis='y', linestyle='--', alpha=0.7)
    

    if value_flag_avg:
        ax3.plot(x_values_avg, avg_values, label="Avg ReTau", color='orange')
        ax3.set_xlabel(x_type_avg)
        ax3.set_ylabel(r"Avg. $Re_{\tau}$")
        ax3.set_title(r"Average $Re_{\tau}$ Values ($t \geq 300$)")
        ax3.set_xticks(x_values_avg)
        ax3.grid(True, alpha=0.7)
    else:
        bars3 = ax3.bar(folders, avg_values)
        ax3.set_title(r"Average Turbulent $Re_{\tau}$ Values ($t \geq 300$)")
        ax3.set_ylabel(r"Avg. $Re_{\tau}$")
        ax3.set_xticklabels(folders, rotation=45, ha='right')
        ax3.grid(axis='y', linestyle='--', alpha=0.7)
    
    
    # Get the full path of the current working directory
    current_working_directory = os.getcwd()

    # Extract just the last part (the directory name)
    directory_name = os.path.basename(current_working_directory)


    plt.tight_layout()
    plt.savefig(f"../ret_plots/retau_summary_{directory_name}.eps")
    if not skip:
        plt.show()


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
    
    
    plt.rcParams['text.usetex'] = True
    
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

    # Check for arguments
    skip = False
    if len(sys.argv) > 2 and sys.argv[2].lower() == "skip":
        skip = True

    if len(sys.argv) < 2 or sys.argv[1].lower() not in ["time", "space","noretau","fast"]:
        print("Usage: python plot_all.py [time|space|noretau|fast] [skip]")
        sys.exit(1)

    # Run the corresponding function based on the argument
    if sys.argv[1].lower() == "space":
        plot_retau_space(folders, current_directory, skip)
        
    elif sys.argv[1].lower() == "time":
        max_retau_time, turbulent_retau_avg = plot_retau_time(folders, current_directory, pickled_plots_names, skip)
        save_retau_data(max_retau_time, turbulent_retau_avg)
        plot_retau_summary(max_retau_time, turbulent_retau_avg, skip)
        
    elif sys.argv[1].lower() == "fast":
        path = os.path.join(current_directory, "retau_data.json")
        print(f"Loading Retau data from {path}")
        max_retau_time, turbulent_retau_avg = read_json_file(path)
        plot_retau_summary(max_retau_time, turbulent_retau_avg, skip)
        
    elif sys.argv[1].lower() == "noretau":
        print("Skipping Retau plot")
        pass
        


        



    
    



