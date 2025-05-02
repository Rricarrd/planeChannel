# Run openfoam case with foamJob
echo "Running case with parameters $name.parameters"
#pyFoamPlotRunner.py --clear --with-courant --no-continuity mpirun -np 6 pimpleFoam -parallel

foamJob -log-app -parallel -wait pimpleFoam


