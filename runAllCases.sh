for dir in *; do
    if [ -f "$dir/runCase.sh" ]; then
    	
    	cd $dir
        echo "Running $dir/runCase.sh"
        bash runCase.sh
        ^c
        cd ..
        pkill -f "python.*plot_all.py"
        python plot_all.py
    fi
done
