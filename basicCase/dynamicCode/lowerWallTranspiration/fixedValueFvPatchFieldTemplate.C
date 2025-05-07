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
#line 20 "/home/rricarrd/OpenFOAM/rricarrd-v2412/run/tfm/planeChannel/basicCase/0/U/boundaryField/bottom"
#include "fvCFD.H"
    #include <cmath>
    #include <iostream>
    #include <complex>
    #include <string>
    #include <fstream>
    #include <vector>
    #include <unordered_map>
    #include <regex>
//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = 05177d541746e5645aea461c297ddf1a43be36a3
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void lowerWallTranspiration_05177d541746e5645aea461c297ddf1a43be36a3(bool load)
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
    lowerWallTranspirationFixedValueFvPatchVectorField
);

} // End namespace Foam


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::
lowerWallTranspirationFixedValueFvPatchVectorField::
lowerWallTranspirationFixedValueFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(p, iF)
{
    if (false)
    {
        printMessage("Construct lowerWallTranspiration : patch/DimensionedField");
    }
}


Foam::
lowerWallTranspirationFixedValueFvPatchVectorField::
lowerWallTranspirationFixedValueFvPatchVectorField
(
    const lowerWallTranspirationFixedValueFvPatchVectorField& rhs,
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const fvPatchFieldMapper& mapper
)
:
    parent_bctype(rhs, p, iF, mapper)
{
    if (false)
    {
        printMessage("Construct lowerWallTranspiration : patch/DimensionedField/mapper");
    }
}


Foam::
lowerWallTranspirationFixedValueFvPatchVectorField::
lowerWallTranspirationFixedValueFvPatchVectorField
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
        printMessage("Construct lowerWallTranspiration : patch/dictionary");
    }
}


Foam::
lowerWallTranspirationFixedValueFvPatchVectorField::
lowerWallTranspirationFixedValueFvPatchVectorField
(
    const lowerWallTranspirationFixedValueFvPatchVectorField& rhs
)
:
    parent_bctype(rhs),
    dictionaryContent(rhs)
{
    if (false)
    {
        printMessage("Copy construct lowerWallTranspiration");
    }
}


Foam::
lowerWallTranspirationFixedValueFvPatchVectorField::
lowerWallTranspirationFixedValueFvPatchVectorField
(
    const lowerWallTranspirationFixedValueFvPatchVectorField& rhs,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(rhs, iF)
{
    if (false)
    {
        printMessage("Construct lowerWallTranspiration : copy/DimensionedField");
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

Foam::
lowerWallTranspirationFixedValueFvPatchVectorField::
~lowerWallTranspirationFixedValueFvPatchVectorField()
{
    if (false)
    {
        printMessage("Destroy lowerWallTranspiration");
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void
Foam::
lowerWallTranspirationFixedValueFvPatchVectorField::updateCoeffs()
{
    if (this->updated())
    {
        return;
    }

    if (false)
    {
        printMessage("updateCoeffs lowerWallTranspiration");
    }

//{{{ begin code
    #line 33 "/home/rricarrd/OpenFOAM/rricarrd-v2412/run/tfm/planeChannel/basicCase/0/U/boundaryField/bottom"
struct local {

        static double addParabolicProfile(
            double H,
            double Ucl,
            double y)
        {
            return ((4.0 * Ucl / (H * H)) * y * (H - y));
        }


        static std::string trim(const std::string& str) {
            size_t first = str.find_first_not_of(" \t\n\r");
            if (std::string::npos == first) {
                return str;
            }
            size_t last = str.find_last_not_of(" \t\n\r");
            return str.substr(first, (last - first + 1));
        }


        // Helper function to remove comments from a line
        static std::string removeComments(const std::string& line) {
            size_t commentPos = line.find("//");
            if (commentPos != std::string::npos) {
                return line.substr(0, commentPos);
            }
            return line;
        }

        // static du_dy
        // {
        //     // Function to calculate the derivative of u with respect to y
        //     double du_dy = 0.0;
        //     // Perform calculations here
        //     return du_dy;
        // }


    };



         // Define parameters
        double w = 0.28175739321266047;
        // double w3d = 0.95;
        // double H = std::stod(parameters["H"]);
        // double Ucl = std::stod(parameters["Ucl"]);
        double L = 5.2359;
        double A = 0.01;
        double k = 2 * 3.141592 / L;
        

        // Creating patch and field data
        const fvPatch& boundaryPatch = patch();
        const vectorField& Cf = boundaryPatch.Cf();
        vectorField& U = *this;

        // Getting current time
        double t = this->db().time().value();

        // Ramp function
        double ramp = min(1, t/5);

        // Getting velocities at the field cells next to the wall
        const tmp<vectorField>& U_field = patchInternalField();
        // Get the face cells, cell centers and face centers
        const labelList& faceCells = patch().faceCells();
        const tmp<vectorField>& cellCenters = patch().boundaryMesh().mesh().C();


        // Calculate u average
        double u_avg = 0;
        double v_avg = 0;

        // Iterating all face cells
        forAll(Cf, faceI)
        {

            // Distance in y direction from face to first cell center
            double dy = cellCenters()[faceCells[faceI]].y();

            // cout << "dy: " << dy << endl;

            // Normal velocity in y direction
            // double uf = U_field()[faceCells[faceI]].x();
            
            // cout << "uf: " << uf << endl;

            // Gradient of ux with respect to the vertical direction y
            // double ub = uf / dy;

            double ub = 4; // In a parabolic profile, at y=0, the derivative with y is du(0)/dy = 4


            // Calculating oscillation and derivative
            double eta = ramp*A*sin(Cf[faceI].x()*k + w*t);
            double d_eta = ramp*A*w*cos(Cf[faceI].x()*k + w*t);
            

            // Calculating velocity components
            double u = -ub*eta;
            double v = d_eta;

            


            // u_avg += u;
            // v_avg += v;


            // Setting boundary conditions
            U[faceI] = vector(u,v,0);
        }

        // Print average velocity
        // u_avg /= Cf.size();
        // v_avg /= Cf.size();
        // std::cout << "Average velocity: " << u_avg << ", " << v_avg << std::endl;
//}}} end code

    this->parent_bctype::updateCoeffs();
}


// ************************************************************************* //

