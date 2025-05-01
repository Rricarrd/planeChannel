#! /bin/sh

## ------ engine:jinja2 ---------

echo "Setting $case field and boundary conditions."

	# Generate files for spatial K-waves
	python initializeCaseFieldBC.py spatial_coded default

	# Set initial field to a parabolic profile using funkySetFields
	funkySetFields -time 0

 

 	
