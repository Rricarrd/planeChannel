#!/bin/bash
tmux new-session -d -s openfoamrun 'bash runAllCases.sh' || tmux attach -t openfoamrun 'bash runAllCases.sh'
