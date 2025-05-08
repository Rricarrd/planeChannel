#!/bin/bash
tmux new-session -d -s openfoamrun 'bash runAllPlotWatchers.sh' || tmux attach -t openfoamrun 'bash runAllPlotWatchers.sh'
