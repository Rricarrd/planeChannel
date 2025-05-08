#!/bin/bash
tmux new-session -d -s openfoamrun 'bash ./runCase.sh' || tmux attach -t openfoamrun 'bash ./runCase.sh'
