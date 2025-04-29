# Attach new tmux session
tmux new -s myfoamrun

# Executing all the runCase.sh options
for dir in *; do
    if [ -f "$dir/runCase.sh" ]; then
    	
    	cd $dir
        echo "Running $dir/runCase.sh using foamJob"
        bash runCase.sh
        cd ..
    fi
done
