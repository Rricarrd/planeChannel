/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2019-2021 OpenCFD Ltd.
    Copyright (C) YEAR AUTHOR, AFFILIATION
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/

#include "fixedValueFvPatchFieldTemplate.H"
#include "addToRunTimeSelectionTable.H"
#include "fvPatchFieldMapper.H"
#include "volFields.H"
#include "surfaceFields.H"
#include "unitConversion.H"
#include "PatchFunction1.H"

//{{{ begin codeInclude
#line 50 "/home/rricarrd/OpenFOAM/rricarrd-v2412/run/tfm/planeChannel/basicCase/0/U/boundaryField/inlet"
#include "fvCFD.H"
                #include <cmath>
                #include <iostream>
                #include <complex>
                #include <string>
                #include <array>
                #include <fstream>
                #include <vector>
                #include <sstream>
                #include <iomanip>
//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = 3f65a80f395a5029bd3774cc0d38d67b786c7202
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void orrSommerfeldInlet_3f65a80f395a5029bd3774cc0d38d67b786c7202(bool load)
{
    if (load)
    {
        // Code that can be explicitly executed after loading
    }
    else
    {
        // Code that can be explicitly executed before unloading
    }
}

// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

makeRemovablePatchTypeField
(
    fvPatchVectorField,
    orrSommerfeldInletFixedValueFvPatchVectorField
);

} // End namespace Foam


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::
orrSommerfeldInletFixedValueFvPatchVectorField::
orrSommerfeldInletFixedValueFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(p, iF)
{
    if (false)
    {
        printMessage("Construct orrSommerfeldInlet : patch/DimensionedField");
    }
}


Foam::
orrSommerfeldInletFixedValueFvPatchVectorField::
orrSommerfeldInletFixedValueFvPatchVectorField
(
    const orrSommerfeldInletFixedValueFvPatchVectorField& rhs,
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const fvPatchFieldMapper& mapper
)
:
    parent_bctype(rhs, p, iF, mapper)
{
    if (false)
    {
        printMessage("Construct orrSommerfeldInlet : patch/DimensionedField/mapper");
    }
}


Foam::
orrSommerfeldInletFixedValueFvPatchVectorField::
orrSommerfeldInletFixedValueFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const dictionary& dict
)
:
    parent_bctype(p, iF, dict)
{
    if (false)
    {
        printMessage("Construct orrSommerfeldInlet : patch/dictionary");
    }
}


Foam::
orrSommerfeldInletFixedValueFvPatchVectorField::
orrSommerfeldInletFixedValueFvPatchVectorField
(
    const orrSommerfeldInletFixedValueFvPatchVectorField& rhs
)
:
    parent_bctype(rhs),
    dictionaryContent(rhs)
{
    if (false)
    {
        printMessage("Copy construct orrSommerfeldInlet");
    }
}


Foam::
orrSommerfeldInletFixedValueFvPatchVectorField::
orrSommerfeldInletFixedValueFvPatchVectorField
(
    const orrSommerfeldInletFixedValueFvPatchVectorField& rhs,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(rhs, iF)
{
    if (false)
    {
        printMessage("Construct orrSommerfeldInlet : copy/DimensionedField");
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

Foam::
orrSommerfeldInletFixedValueFvPatchVectorField::
~orrSommerfeldInletFixedValueFvPatchVectorField()
{
    if (false)
    {
        printMessage("Destroy orrSommerfeldInlet");
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void
Foam::
orrSommerfeldInletFixedValueFvPatchVectorField::updateCoeffs()
{
    if (this->updated())
    {
        return;
    }

    if (false)
    {
        printMessage("updateCoeffs orrSommerfeldInlet");
    }

//{{{ begin code
    #line 64 "/home/rricarrd/OpenFOAM/rricarrd-v2412/run/tfm/planeChannel/basicCase/0/U/boundaryField/inlet"
// Creating patch and field data
                const fvPatch& boundaryPatch = patch();
                const vectorField& Cf = boundaryPatch.Cf();
                vectorField& field = *this;

                // Getting current time
                scalar t = this->db().time().value();


                // Read the polynomial regressions coefficients dict

                // IOobject polyReg
                // (
                //     "polynomialRegressionCoefficients",    // dictionary name
                //     "/home/rricarrd/OpenFOAM/rricarrd-v2412/run/tfm/planeChannel/basicCase/constant",     // dict is found in "constant"
                //     patch(),                   // registry for the dict
                //     IOobject::MUST_READ,    // must exist, otherwise failure
                //     IOobject::NO_WRITE      // dict is only read by the solver
                // );
                //
                // IOdictionary polyCoeffsDict(polyReg);
                //
                // // Save coefficients to vectors
                // UList u2dCoeffs
                // (
                //     polyCoeffsDict.lookup("u2d")
                // );


                // Read file directly
                std::ifstream inputFile("constant/polynomialRegressions"); // Open the file

                std::array<std::array<double, 20>, 6> coeffs_array;

                // Iterate along the file lines
                if (inputFile.is_open()) {
                    std::string line;
                    // Iterate lines
                    int i = 0;
                    while (std::getline(inputFile, line)) {
                        // Initialize string stream for the current line
                        std::stringstream ss(line);
                        double value;

                        // For each line iterate along the elements of the string
                        int j = 0;
                        while (ss >> value) {
                            // Potential Error 1: Bounds checking for j
                            if (j < 20) {
                                coeffs_array[i][j] = value;
                                j++;
                            } else {
                                std::cerr << "Warning: Line " << i + 1 << " has more than 20 values. Ignoring extra values." << std::endl;
                                // Optionally, you could break out of the inner loop here if you only want the first 20.
                            }
                        }

                        i++;
                        // Potential Error 2: Bounds checking for i
                        if (i >= 6) {
                            std::cerr << "Warning: File has more than 6 lines. Ignoring extra lines." << std::endl;
                            break; // Stop reading further lines
                        }
                    }
                    inputFile.close(); // Close the file
                } else {
                    std::cerr << "Unable to open file: constant/polynomialRegressions" << std::endl;
                }



                // Iterating all face cells
                forAll(Cf, faceI)
                {
                field[faceI] = vector(1,0,0);
                }
//}}} end code

    this->parent_bctype::updateCoeffs();
}


// ************************************************************************* //

