#! /bin/sh

## ------ engine:jinja2 ---------

echo "Setting $case field and boundary conditions."

	# Generate time varying inlet K-waves for the whole simulation
	python initializeCaseFieldBC.py temporal default
	

 


   	rm -f constant/dynamicMeshDict
   	rm -f 0/cellDisplacement
   	rm -f 0/pointDisplacement
 	
