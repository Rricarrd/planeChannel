# Run openfoam case with foamJob
echo "Running case with parameters $name.parameters"
mpirun -np 6 pimpleFoam -parallel

# Ensure MPI processes are cleaned up
echo "Cleaning up MPI processes..."
killall -9 mpirun || echo "No MPI processes to clean up."

# Running plotWatcher
pyFoamPlotWatcher.py --solver-not-running-anymore log.pimpleFoam || echo "Error occurred executing the pyFoamPlotWatcher.py!"
