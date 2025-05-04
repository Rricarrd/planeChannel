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

#include "fixedValuePointPatchFieldTemplate.H"
#include "addToRunTimeSelectionTable.H"
#include "pointPatchFieldMapper.H"
#include "pointFields.H"
#include "unitConversion.H"
#include "PatchFunction1.H"

//{{{ begin codeInclude
#line 48 "/home/rricarrd/OpenFOAM/rricarrd-v2406/tfm/planeChannel/basicCase/0/pointDisplacement/boundaryField/bottom"
#include "fvCFD.H"
        #include "pointFields.H"
        #include "primitivePatchInterpolation.H"
        #include <cmath>
        #include <iostream>
        #include <vector>
//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = ae78ca5958e8f022d635aa96f616d989d9977772
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void movingLowerWallPoints_ae78ca5958e8f022d635aa96f616d989d9977772(bool load)
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

makePointPatchTypeField
(
    pointPatchVectorField,
    movingLowerWallPointsFixedValuePointPatchVectorField
);

} // End namespace Foam


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::
movingLowerWallPointsFixedValuePointPatchVectorField::
movingLowerWallPointsFixedValuePointPatchVectorField
(
    const pointPatch& p,
    const DimensionedField<vector, pointMesh>& iF
)
:
    parent_bctype(p, iF)
{
    if (false)
    {
        printMessage("Construct movingLowerWallPoints : patch/DimensionedField");
    }
}


Foam::
movingLowerWallPointsFixedValuePointPatchVectorField::
movingLowerWallPointsFixedValuePointPatchVectorField
(
    const movingLowerWallPointsFixedValuePointPatchVectorField& rhs,
    const pointPatch& p,
    const DimensionedField<vector, pointMesh>& iF,
    const pointPatchFieldMapper& mapper
)
:
    parent_bctype(rhs, p, iF, mapper)
{
    if (false)
    {
        printMessage("Construct movingLowerWallPoints : patch/DimensionedField/mapper");
    }
}


Foam::
movingLowerWallPointsFixedValuePointPatchVectorField::
movingLowerWallPointsFixedValuePointPatchVectorField
(
    const pointPatch& p,
    const DimensionedField<vector, pointMesh>& iF,
    const dictionary& dict,
    IOobjectOption::readOption requireValue
)
:
    parent_bctype(p, iF, dict, requireValue)
{
    if (false)
    {
        printMessage("Construct movingLowerWallPoints : patch/dictionary");
    }
}


Foam::
movingLowerWallPointsFixedValuePointPatchVectorField::
movingLowerWallPointsFixedValuePointPatchVectorField
(
    const movingLowerWallPointsFixedValuePointPatchVectorField& rhs
)
:
    parent_bctype(rhs),
    dictionaryContent(rhs)
{
    if (false)
    {
        printMessage("Copy construct movingLowerWallPoints");
    }
}


Foam::
movingLowerWallPointsFixedValuePointPatchVectorField::
movingLowerWallPointsFixedValuePointPatchVectorField
(
    const movingLowerWallPointsFixedValuePointPatchVectorField& rhs,
    const DimensionedField<vector, pointMesh>& iF
)
:
    parent_bctype(rhs, iF)
{
    if (false)
    {
        printMessage("Construct movingLowerWallPoints : copy/DimensionedField");
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

Foam::
movingLowerWallPointsFixedValuePointPatchVectorField::
~movingLowerWallPointsFixedValuePointPatchVectorField()
{
    if (false)
    {
        printMessage("Destroy movingLowerWallPoints");
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void
Foam::
movingLowerWallPointsFixedValuePointPatchVectorField::updateCoeffs()
{
    if (this->updated())
    {
        return;
    }

    if (false)
    {
        printMessage("updateCoeffs movingLowerWallPoints");
    }

//{{{ begin code
    #line 59 "/home/rricarrd/OpenFOAM/rricarrd-v2406/tfm/planeChannel/basicCase/0/pointDisplacement/boundaryField/bottom"
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

