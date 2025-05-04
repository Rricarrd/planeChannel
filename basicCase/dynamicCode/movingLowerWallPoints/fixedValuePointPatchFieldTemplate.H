/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2019-2021 OpenCFD Ltd.
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

Description
    Template for use with dynamic code generation of a
    fixedValue pointPatchField.

    - without state

SourceFiles
    fixedValuePointPatchFieldTemplate.C

\*---------------------------------------------------------------------------*/

#ifndef coded_fixedValuePointPatchTemplateVectorField_H
#define coded_fixedValuePointPatchTemplateVectorField_H

#include "fixedValuePointPatchFields.H"
#include "dictionaryContent.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

/*---------------------------------------------------------------------------*\
                A templated FixedValuePointPatchField
\*---------------------------------------------------------------------------*/

class movingLowerWallPointsFixedValuePointPatchVectorField
:
    public fixedValuePointPatchField<vector>,
    public dictionaryContent
{
    //- The parent boundary condition type
    typedef fixedValuePointPatchField<vector> parent_bctype;


    // Private Member Functions

        //- Report a message with the SHA1sum
        inline static void printMessage(const char* message)
        {
            Info<< message << " sha1: " << SHA1sum << '\n';
        }

public:

    //- SHA1 representation of the code content
    static constexpr const char* const SHA1sum = "ae78ca5958e8f022d635aa96f616d989d9977772";

    //- Runtime type information
    TypeName("movingLowerWallPoints");


    // Constructors

        //- Construct from patch and internal field
        movingLowerWallPointsFixedValuePointPatchVectorField
        (
            const pointPatch&,
            const DimensionedField<vector, pointMesh>&
        );

        //- Construct from patch, internal field and dictionary
        movingLowerWallPointsFixedValuePointPatchVectorField
        (
            const pointPatch&,
            const DimensionedField<vector, pointMesh>&,
            const dictionary& dict,
            IOobjectOption::readOption requireValue = IOobjectOption::MUST_READ
        );

        //- Construct by mapping a copy onto a new patch
        movingLowerWallPointsFixedValuePointPatchVectorField
        (
            const movingLowerWallPointsFixedValuePointPatchVectorField&,
            const pointPatch&,
            const DimensionedField<vector, pointMesh>&,
            const pointPatchFieldMapper&
        );

        //- Construct as copy
        movingLowerWallPointsFixedValuePointPatchVectorField
        (
            const movingLowerWallPointsFixedValuePointPatchVectorField&
        );

        //- Construct as copy setting internal field reference
        movingLowerWallPointsFixedValuePointPatchVectorField
        (
            const movingLowerWallPointsFixedValuePointPatchVectorField&,
            const DimensionedField<vector, pointMesh>&
        );

        //- Return a clone
        virtual autoPtr<pointPatchField<vector>> clone() const
        {
            return pointPatchField<vector>::Clone(*this);
        }

        //- Construct and return a clone setting internal field reference
        virtual autoPtr<pointPatchField<vector>> clone
        (
            const DimensionedField<vector, pointMesh>& iF
        ) const
        {
            return pointPatchField<vector>::Clone(*this, iF);
        }


    //- Destructor
    virtual ~movingLowerWallPointsFixedValuePointPatchVectorField();


    // Member Functions

        //- Code context as a dictionary
        const dictionary& codeContext() const noexcept
        {
            return dictionaryContent::dict();
        }

        //- Update the coefficients associated with the patch field
        virtual void updateCoeffs();
};


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#endif

// ************************************************************************* //

