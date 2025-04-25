# Run openfoam case with PyFoam
echo "Running case with parameters $name.parameters"
pyFoamPlotRunner.py --clear --with-courant --no-continuity mpirun -np 16 moveDynamicMesh -parallel
