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
// SHA1 = 0aa72166855daf743d2ea4216a469a452bfb1795
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void movingLowerWallPoints_0aa72166855daf743d2ea4216a469a452bfb1795(bool load)
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
//- Get this field
        vectorField& field = *this;

        //- Get the cell displacement field
        const volVectorField& cellDisplacement = this->db().lookupObject<volVectorField>("cellDisplacement");
        const fvMesh & mesh  =  cellDisplacement.mesh();
        
        //- PatchID 
        const label patchID = mesh.boundaryMesh().findPatchID("bottom");
        if (patchID < 0)
        {
            FatalError
                << "Cannot find patch named 'bottom'"
                << exit(FatalError);
        }

        //- set-up interpolator
        primitivePatchInterpolation patchInterpolator
        (
            mesh.boundaryMesh()[patchID]
        );

        //- Get cell displacement face values 
        const vectorField& cellDisplacementFaceValues = cellDisplacement.boundaryField()[patchID];

        //- Perform interpolation 
        const vectorField& cellDisplacementFaceValuesInterpolated = patchInterpolator.interpolate(cellDisplacementFaceValues);





        
        
        Info<< "Updated bottom boundary displacement field" << endl;
//}}} end code

    this->parent_bctype::updateCoeffs();
}


// ************************************************************************* //

