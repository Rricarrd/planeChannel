# Run openfoam case with foamJob
echo "Running case with parameters $name.parameters"
#pyFoamPlotRunner.py --clear --with-courant --no-continuity mpirun -np 6 moveDynamicMesh -parallel

foamJob -log-app -parallel -wait moveDynamicMesh

# Running plotWatcher
pyFoamPlotWatcher.py log.moveDynamicMesh || echo "Error occurred executing the pyFoamPlotWatcher.py!"
