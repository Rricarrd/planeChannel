import os
import pathlib
import sys
import argparse
import openfoamparser as Ofpp
import numpy as np

# Functions
def calculate_omega(parsed_data, current_path, parameters_file_name):
    if parsed_data['freqFromOrr'] == 'yes':
        omega = np.real(generate_initial_field.calculate_omega(parsed_data,current_path))
        print(f"Omega calculated from Orr-Sommerfeld equation: {omega}")
        data_to_substitute = {'omega': omega}
        parameters_file_path = os.path.join(current_path,parameters_file_name)
        parsing.substitute_in_parameters(data_to_substitute,parameters_file_path)


# Main code
current_path = pathlib.Path().resolve() # Get current path
parent_path = pathlib.Path().resolve().parent # Get parent path
sys.path.append(str(parent_path)) # Add to python path to access scripts folder
sys.path.append(str(parent_path.parent)) # Add to python path to access scripts folder

# Now import the scripts folder
from scripts.field import generate_initial_field
from scripts.inlet import generate_initial_inlet
from scripts.inlet import generate_profiles_inlet
from scripts.common import parsing

# Parse CLI commands
parser = argparse.ArgumentParser(description="Initialization Python script for the planeChannel turbulent transition case")
parser.add_argument("type", type=str, help="Type of initialization: either inletBC or initialField")
parser.add_argument("parameters_file", type=str, help="Parameters file name")
args = parser.parse_args()

# Parse data from a .parameters file
if args.parameters_file:
    parameters_file_name = f"{args.parameters_file}.parameters"
else:
    parameters_file_name = f"default.parameters"

print(f"Getting values from {parameters_file_name}")
parsed_data = parsing.parse_foam_file(os.path.join(current_path,parameters_file_name))

# Extracting current mesh cell centres
cell_centres=Ofpp.parse_internal_field(f'{str(current_path)}/constant/C')


# Generating the corresponding initial conditions
if args.type == "spatial":
    # Generate time varying inlet for spatial changing simulation
    generate_initial_inlet.generate(parsed_data,current_path,cell_centres)
    calculate_omega(parsed_data, current_path, parameters_file_name)

elif args.type == "spatial_coded":
    # Generate velocities Orr sommerfeld velocity profiles for the inlet
    generate_profiles_inlet.generate(parsed_data,current_path,cell_centres)
    calculate_omega(parsed_data, current_path, parameters_file_name)


elif args.type == "temporal":
    # Generate spatailly varying field for the time changing simulation
    generate_initial_field.generate(parsed_data,current_path,cell_centres)
    calculate_omega(parsed_data, current_path, parameters_file_name)

else:
    print("Incorrect type initialization. Choose either inletBC or initialField")
    


