#!\bin\sh

echo "Clearing the case using foam"
pyFoamClearCase.py --keep-dynamic-code . 

echo "Removing mesh and initial conditions"
rm -r "./constant/boundaryData"
rm -r "./constant/polyMesh"


echo "Finding and removing directories matching the pattern processor[0-9]+"
find . -type d -regextype posix-extended -regex ".*/processor[0-9]+" -exec rm -r {} +

echo "Finding and removing other directories"
find . -type d -regextype posix-extended -regex ".*/*.analyzed" -exec rm -r {} +


# Check for all argument
if [[ " $@ " == *" -all "* ]]; then
    # Remove other files
    rm -f *.png 
    rm -f *.log 
    rm -f PyFoam*
    rm -rf *.rst
fi

echo "Case cleaned"
