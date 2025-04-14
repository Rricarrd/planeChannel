for dir in *; do
    if [ -f "$dir/runCase.sh" ]; then
    	
    	cd $dir
        echo "Running $dir/runCase.sh"
        bash runCase.sh
        ^c
        cd ..
        pkill -f "python.*plot_all.py"
        killall gnuplot_x11
        python plot_all.py
    fi
done
