import os
import pickle
import matplotlib.pyplot as plt
import json
import openfoamparser as Ofpp
import numpy as np
import re
import sys


def extract_number(name):
    num = ""
    for char in name:
        if char.isdigit():
            num += char
        else:
            break
    return int(num) if num else 0



def print_retau_time(folders, current_directory, plots_names):
    print("Printing Retau time")

    # Create a simple matplotlib figure
    fig, ax = plt.subplots()
    ax.set_title("Channel Ret over time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Ret")


    # Iterate through each folder and check for the pickled file
    for folder in folders:
        pickled_file_path = os.path.join(current_directory, folder, "Gnuplotting.analyzed/pickledPlots")
        print(f"Checking folder: {folder}")
        print(f"Pickled file path: {pickled_file_path}")

        if folder[0].isdigit() and os.path.exists(pickled_file_path):
            try:
                with open(pickled_file_path, "rb") as file:
                    data = pickle.load(file)

                

                    ret = data[plots_names['ReTau']]['values']['avg']
                    times = data[plots_names['ReTau']]['times']


                    folder_name = re.sub(r'^\d+_', '', folder)
                    folder_name = folder_name.capitalize()

                    ax.plot(times, ret, label=folder_name)
                    

            except KeyError as e:
                print(f"KeyError: {e} in folder: {folder}")

    # Reference data DNS
    times_dns = [9.79765708200213, 25.559105431309906, 42.17252396166134, 57.082002129925456, 69.43556975505858, 82.64110756123536, 95.42066027689032, 107.77422790202344, 117.14589989350374, 126.0915867944622, 132.48136315228967, 138.0191693290735, 142.2790202342918, 145.26091586794462, 147.3908413205538, 150.3727369542066, 152.50266240681577, 155.05857294994675, 158.0404685835996, 160.17039403620873, 162.72630457933974, 165.28221512247072, 167.83812566560172, 170.3940362087327, 172.09797657082004, 175.07987220447285, 178.06176783812566, 180.19169329073483, 183.17358892438764, 188.71139510117146, 193.82321618743345, 197.2310969116081, 201.0649627263046, 201.49094781682643, 207.02875399361022, 210.86261980830673, 217.2523961661342, 223.21618743343984, 227.47603833865816, 233.86581469648564, 237.69968051118212, 241.10756123535677, 247.07135250266242, 256.8690095846645, 261.98083067092654, 266.6666666666667, 272.2044728434505, 276.038338658147, 282.8541001064963, 289.66986155484557, 294.7816826411076, 299.89350372736953, 309.26517571884983, 316.93290734824285, 330.1384451544196, 335.67625133120345, 341.21405750798726, 345.8998935037274, 351.86368477103304, 361.66134185303514, 374.0149094781683, 380.8306709265176, 382.96059637912674, 386.7944621938232, 390.6283280085197, 397.44408945686905]
    ret_dns = [101.14503816793894, 101.6030534351145, 101.6030534351145, 101.37404580152672, 101.37404580152672, 101.14503816793894, 101.37404580152672, 102.29007633587786, 104.12213740458016, 107.32824427480917, 112.13740458015268, 117.17557251908397, 121.98473282442748, 128.62595419847327, 133.89312977099237, 140.53435114503816, 149.9236641221374, 160.2290076335878, 179.92366412213738, 194.35114503816794, 205.34351145038167, 219.08396946564886, 227.09923664122135, 236.2595419847328, 242.90076335877862, 244.50381679389312, 242.67175572519085, 238.54961832061068, 233.2824427480916, 223.66412213740458, 221.83206106870227, 218.62595419847327, 213.3587786259542, 209.6946564885496, 209.46564885496184, 208.0916030534351, 203.51145038167937, 201.6793893129771, 201.22137404580153, 202.59541984732823, 204.42748091603053, 204.8854961832061, 204.19847328244276, 206.4885496183206, 205.34351145038167, 204.19847328244276, 204.6564885496183, 207.17557251908397, 207.63358778625954, 207.17557251908397, 206.71755725190837, 207.40458015267177, 209.23664122137404, 210.61068702290078, 210.83969465648855, 211.5267175572519, 213.81679389312978, 211.5267175572519, 210.61068702290078, 207.63358778625954, 207.8625954198473, 208.0916030534351, 209.00763358778624, 210.61068702290078, 211.29770992366412, 212.44274809160305]

    ax.scatter(times_dns, ret_dns, label="DNS")
            
    plt.legend()
    plt.savefig("variations_ret.png")
    plt.show()

def print_retau_space(folders, current_directory):
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
                ax.scatter(x,ret, label=f"{folder}")


            except KeyError as e:
                print(f"KeyError: {e} in folder: {folder}")

    # Reference data DNS
    # times_dns = [9.79765708200213, 25.559105431309906, 42.17252396166134, 57.082002129925456, 69.43556975505858, 82.64110756123536, 95.42066027689032, 107.77422790202344, 117.14589989350374, 126.0915867944622, 132.48136315228967, 138.0191693290735, 142.2790202342918, 145.26091586794462, 147.3908413205538, 150.3727369542066, 152.50266240681577, 155.05857294994675, 158.0404685835996, 160.17039403620873, 162.72630457933974, 165.28221512247072, 167.83812566560172, 170.3940362087327, 172.09797657082004, 175.07987220447285, 178.06176783812566, 180.19169329073483, 183.17358892438764, 188.71139510117146, 193.82321618743345, 197.2310969116081, 201.0649627263046, 201.49094781682643, 207.02875399361022, 210.86261980830673, 217.2523961661342, 223.21618743343984, 227.47603833865816, 233.86581469648564, 237.69968051118212, 241.10756123535677, 247.07135250266242, 256.8690095846645, 261.98083067092654, 266.6666666666667, 272.2044728434505, 276.038338658147, 282.8541001064963, 289.66986155484557, 294.7816826411076, 299.89350372736953, 309.26517571884983, 316.93290734824285, 330.1384451544196, 335.67625133120345, 341.21405750798726, 345.8998935037274, 351.86368477103304, 361.66134185303514, 374.0149094781683, 380.8306709265176, 382.96059637912674, 386.7944621938232, 390.6283280085197, 397.44408945686905]
    # ret_dns = [101.14503816793894, 101.6030534351145, 101.6030534351145, 101.37404580152672, 101.37404580152672, 101.14503816793894, 101.37404580152672, 102.29007633587786, 104.12213740458016, 107.32824427480917, 112.13740458015268, 117.17557251908397, 121.98473282442748, 128.62595419847327, 133.89312977099237, 140.53435114503816, 149.9236641221374, 160.2290076335878, 179.92366412213738, 194.35114503816794, 205.34351145038167, 219.08396946564886, 227.09923664122135, 236.2595419847328, 242.90076335877862, 244.50381679389312, 242.67175572519085, 238.54961832061068, 233.2824427480916, 223.66412213740458, 221.83206106870227, 218.62595419847327, 213.3587786259542, 209.6946564885496, 209.46564885496184, 208.0916030534351, 203.51145038167937, 201.6793893129771, 201.22137404580153, 202.59541984732823, 204.42748091603053, 204.8854961832061, 204.19847328244276, 206.4885496183206, 205.34351145038167, 204.19847328244276, 204.6564885496183, 207.17557251908397, 207.63358778625954, 207.17557251908397, 206.71755725190837, 207.40458015267177, 209.23664122137404, 210.61068702290078, 210.83969465648855, 211.5267175572519, 213.81679389312978, 211.5267175572519, 210.61068702290078, 207.63358778625954, 207.8625954198473, 208.0916030534351, 209.00763358778624, 210.61068702290078, 211.29770992366412, 212.44274809160305]

    #ax.scatter(times_dns, ret_dns, label="DNS")
            

    ax.set_title(f"Channel Ret over space at time {last_time}")

    plt.legend()
    plt.savefig("variations_ret.png")
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

    # Check for arguments
    if len(sys.argv) != 2 or sys.argv[1].lower() not in ["time", "space"]:
        print("Usage: python plot_all.py [time|space]")
        sys.exit(1)

    # Run the corresponding function based on the argument
    if sys.argv[1].lower() == "space":
        print_retau_space(folders, current_directory)
    else:
        print_retau_time(folders, current_directory, pickled_plots_names)






