#! /bin/sh
## ------ engine:jinja2 ---------

echo "Preparing files for decomposePar"


	echo "Removing templates from 0"
	rm 0/*.template
	
	echo "Copying .finalTemplates into 0.tmp"
	mkdir 0.tmp
	mv 0/*.finalTemplate 0.tmp
	
	pyFoamDecompose.py . 6
	
	echo "Copying 0.tmp back into each processor folder"
	
		cp 0.tmp/* processor0/0/
	
		cp 0.tmp/* processor1/0/
	
		cp 0.tmp/* processor2/0/
	
		cp 0.tmp/* processor3/0/
	
		cp 0.tmp/* processor4/0/
	
		cp 0.tmp/* processor5/0/
	

	echo "Deleting 0.tmp"
	rm -r 0.tmp

