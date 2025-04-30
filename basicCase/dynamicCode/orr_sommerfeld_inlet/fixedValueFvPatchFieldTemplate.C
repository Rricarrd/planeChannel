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
//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = 6adf9084186581a9b40141c4da9e5fd30357e15c
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void orr_sommerfeld_inlet_6adf9084186581a9b40141c4da9e5fd30357e15c(bool load)
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
    orr_sommerfeld_inletFixedValueFvPatchVectorField
);

} // End namespace Foam


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

Foam::
orr_sommerfeld_inletFixedValueFvPatchVectorField::
orr_sommerfeld_inletFixedValueFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(p, iF)
{
    if (false)
    {
        printMessage("Construct orr_sommerfeld_inlet : patch/DimensionedField");
    }
}


Foam::
orr_sommerfeld_inletFixedValueFvPatchVectorField::
orr_sommerfeld_inletFixedValueFvPatchVectorField
(
    const orr_sommerfeld_inletFixedValueFvPatchVectorField& rhs,
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const fvPatchFieldMapper& mapper
)
:
    parent_bctype(rhs, p, iF, mapper)
{
    if (false)
    {
        printMessage("Construct orr_sommerfeld_inlet : patch/DimensionedField/mapper");
    }
}


Foam::
orr_sommerfeld_inletFixedValueFvPatchVectorField::
orr_sommerfeld_inletFixedValueFvPatchVectorField
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
        printMessage("Construct orr_sommerfeld_inlet : patch/dictionary");
    }
}


Foam::
orr_sommerfeld_inletFixedValueFvPatchVectorField::
orr_sommerfeld_inletFixedValueFvPatchVectorField
(
    const orr_sommerfeld_inletFixedValueFvPatchVectorField& rhs
)
:
    parent_bctype(rhs),
    dictionaryContent(rhs)
{
    if (false)
    {
        printMessage("Copy construct orr_sommerfeld_inlet");
    }
}


Foam::
orr_sommerfeld_inletFixedValueFvPatchVectorField::
orr_sommerfeld_inletFixedValueFvPatchVectorField
(
    const orr_sommerfeld_inletFixedValueFvPatchVectorField& rhs,
    const DimensionedField<vector, volMesh>& iF
)
:
    parent_bctype(rhs, iF)
{
    if (false)
    {
        printMessage("Construct orr_sommerfeld_inlet : copy/DimensionedField");
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

Foam::
orr_sommerfeld_inletFixedValueFvPatchVectorField::
~orr_sommerfeld_inletFixedValueFvPatchVectorField()
{
    if (false)
    {
        printMessage("Destroy orr_sommerfeld_inlet");
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void
Foam::
orr_sommerfeld_inletFixedValueFvPatchVectorField::updateCoeffs()
{
    if (this->updated())
    {
        return;
    }

    if (false)
    {
        printMessage("updateCoeffs orr_sommerfeld_inlet");
    }

//{{{ begin code
    #line 60 "/home/rricarrd/OpenFOAM/rricarrd-v2412/run/tfm/planeChannel/basicCase/0/U/boundaryField/inlet"
// Creating patch and field data
                const fvPatch& boundaryPatch = patch();
                const vectorField& Cf = boundaryPatch.Cf();
                vectorField& field = *this;

                // Getting current time
                scalar t = this->db().time().value();


                //// Read the filename parameter
                // Provide an absolute path.
                const fileName dataFileName = this->db().lookupObject<fileName>("constant/velocityProfiles/polynomialRegressions");
                // Construct path relative to the case directory using time info
                const fileName casePath = this->db().time().path().parentPath();
                const fileName absoluteDataFilePath = casePath/dataFileName;

                Info << "Reading boundary data for patch " << patch.name()
                    << " from file " << absoluteDataFilePath << endl;

                // Use OpenFOAM's IFstream for better integration
                Foam::IFstream dataStream(absoluteDataFilePath);

                // Check if file opened successfully
                if (!dataStream.good())
                {
                    FatalErrorInFunction
                        << "Cannot open data file " << absoluteDataFilePath << nl
                        << "Check path and permissions."
                        << abort(FatalError);
                }


                // Iterating all face cells
                forAll(Cf, faceI)
                {
                field[faceI] = vector(sin(t)*U_0*(1-(pow(Cf[faceI].y()-p_ctr,2))/(p_r*p_r))),0,0);
                }
//}}} end code

    this->parent_bctype::updateCoeffs();
}


// ************************************************************************* //

