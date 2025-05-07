# Executing all the runCase.sh options
for dir in *; do
    if [ -f "$dir/runCase.sh" ]; then
    	
    	cd $dir
        echo "Running $dir/runPlotWatcher.py using pyFoam"
        bash runPlotWatcher.sh
        cd ..
    fi
done
