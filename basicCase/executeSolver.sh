# Run openfoam case with foamJob
echo "Running case with parameters $name.parameters"
#pyFoamPlotRunner.py --clear --with-courant --no-continuity mpirun -np 6 pimpleFoam -parallel

nohup foamJob -log-app -parallel -wait pimpleFoam

# Running plotWatcher
pyFoamPlotWatcher.py log.pimpleFoam || echo "Error occurred executing the pyFoamPlotWatcher.py!"
