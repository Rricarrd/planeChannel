#!/bin/bash/

# Running plotWatcher
pyFoamPlotWatcher.py --solver-not-running-anymore log.pimpleFoam || echo "Error occurred executing the pyFoamPlotWatcher.py!"
