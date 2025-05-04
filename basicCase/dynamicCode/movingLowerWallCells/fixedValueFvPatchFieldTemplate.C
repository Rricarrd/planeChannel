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
#line 47 "/home/rricarrd/OpenFOAM/rricarrd-v2406/tfm/planeChannel/basicCase/0/cellDisplacement/boundaryField/bottom"
#include "fvCFD.H"
        #include <cmath>
        #include <iostream>
        #include <vector>
        #include <fstream>
        #include <string>
        #include <regex>
        #include <unordered_map>
//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = 4b1e03a26e10eb039c4f4d7d794cc44b74347be6
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void movingLowerWallCells_4b1e03a26e10eb039c4f4d7d794cc44b74347be6(bool load)
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
    movingLowerWallCellsFixedValueFvPatchVectorField
);

} // End namespace Foam


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::
movingLowerWallCellsFixedValueFvPatchVectorField::
movingLowerWallCellsFixedValueFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(p, iF)
{
    if (false)
    {
        printMessage("Construct movingLowerWallCells : patch/DimensionedField");
    }
}


Foam::
movingLowerWallCellsFixedValueFvPatchVectorField::
movingLowerWallCellsFixedValueFvPatchVectorField
(
    const movingLowerWallCellsFixedValueFvPatchVectorField& rhs,
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const fvPatchFieldMapper& mapper
)
:
    parent_bctype(rhs, p, iF, mapper)
{
    if (false)
    {
        printMessage("Construct movingLowerWallCells : patch/DimensionedField/mapper");
    }
}


Foam::
movingLowerWallCellsFixedValueFvPatchVectorField::
movingLowerWallCellsFixedValueFvPatchVectorField
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
        printMessage("Construct movingLowerWallCells : patch/dictionary");
    }
}


Foam::
movingLowerWallCellsFixedValueFvPatchVectorField::
movingLowerWallCellsFixedValueFvPatchVectorField
(
    const movingLowerWallCellsFixedValueFvPatchVectorField& rhs
)
:
    parent_bctype(rhs),
    dictionaryContent(rhs)
{
    if (false)
    {
        printMessage("Copy construct movingLowerWallCells");
    }
}


Foam::
movingLowerWallCellsFixedValueFvPatchVectorField::
movingLowerWallCellsFixedValueFvPatchVectorField
(
    const movingLowerWallCellsFixedValueFvPatchVectorField& rhs,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(rhs, iF)
{
    if (false)
    {
        printMessage("Construct movingLowerWallCells : copy/DimensionedField");
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

Foam::
movingLowerWallCellsFixedValueFvPatchVectorField::
~movingLowerWallCellsFixedValueFvPatchVectorField()
{
    if (false)
    {
        printMessage("Destroy movingLowerWallCells");
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void
Foam::
movingLowerWallCellsFixedValueFvPatchVectorField::updateCoeffs()
{
    if (this->updated())
    {
        return;
    }

    if (false)
    {
        printMessage("updateCoeffs movingLowerWallCells");
    }

//{{{ begin code
    #line 59 "/home/rricarrd/OpenFOAM/rricarrd-v2406/tfm/planeChannel/basicCase/0/cellDisplacement/boundaryField/bottom"
// Creating patch and field data
        const fvPatch& boundaryPatch = patch();
        const vectorField& Cf = boundaryPatch.Cf();
        vectorField& field = *this;

        // Getting current time
        double t = this->db().time().value();


        // Set variables
        const scalar A = 0.5;
        const scalar k = 2 * 3.141592 / 80;
        const scalar f = 0.2817573932125998;
        const scalar ramp = min(t / 15.0, 1.0);
        const scalarField& X = Cf.component(vector::X);


        // Loop over the faces of the patch
        forAll(Cf, faceI)
        { 
            field[faceI] = vector(0, A * sin(k * X[faceI] + f * t), 0);
        }
//}}} end code

    this->parent_bctype::updateCoeffs();
}


// ************************************************************************* //

