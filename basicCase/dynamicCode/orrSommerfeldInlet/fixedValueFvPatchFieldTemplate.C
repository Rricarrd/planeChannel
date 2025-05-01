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
                #include <fstream>
                #include <vector>
                #include <sstream>
//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = 3d229fca55ddc07a5d02652d9aba631d2d3faa14
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void orrSommerfeldInlet_3d229fca55ddc07a5d02652d9aba631d2d3faa14(bool load)
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
    #line 62 "/home/rricarrd/OpenFOAM/rricarrd-v2412/run/tfm/planeChannel/basicCase/0/U/boundaryField/inlet"
struct local {
                // Evaluate polynomial function
                static double evaluatePolynomial
                (
                    const std::vector<double>& coefficients,
                    double y
                )
                    {
                        double result = 0.0;
                        for (size_t i = 0; i < coefficients.size(); ++i)
                            {
                            result += coefficients[i] * std::pow(y, i);
                            }
                        return result;
                    }



                // Function to calculate the real part of a complex number
                static double realPart(const std::complex<double>& y)
                {
                    return std::real(y);
                }


                // Function to calculate the u_hat values based on y and component index
                static std::complex<double> calculate_u_hat(
                    const std::vector<double>& real_coefficients,
                    const std::vector<double>& imag_coefficients,
                    double y)
                    {
                        double real_part = evaluatePolynomial(real_coefficients, y);
                        double imag_part = evaluatePolynomial(imag_coefficients, y);
                        return std::complex<double>(real_part, imag_part);
                    }

                // Function to implement the equation for a single spatial component
                static double calculate_u_tilde_component(
                    double y,
                    double z,
                    double t,
                    double A_2d,
                    double omega_r2d,
                    double A_3d,
                    double beta,
                    double omega_r3d,
                    const std::vector<double>& u_r2d_coefficients,
                    const std::vector<double>& u_r2di_coefficients,
                    const std::vector<double>& u_r3d_coefficients,
                    const std::vector<double>& u_r3di_coefficients)
                    {
                        std::complex<double> term1_exponential = exp(std::complex<double>(0.0, -omega_r2d * t));
                        std::complex<double> term2_exponential = exp(std::complex<double>(0.0, beta * z - omega_r3d * t));
                        std::complex<double> term3_exponential = exp(std::complex<double>(0.0, -beta * z - omega_r3d * t)); // Assuming the '-' sign was intended

                        std::complex<double> u_hat_r2d_y = calculate_u_hat(u_r2d_coefficients, u_r2di_coefficients, y);
                        std::complex<double> u_hat_plus_r3d_y = calculate_u_hat(u_r3d_coefficients, u_r3di_coefficients, y);
                        std::complex<double> u_hat_minus_r3d_y = calculate_u_hat(u_r3d_coefficients, u_r3di_coefficients, y);

                        double term1 = A_2d * realPart(u_hat_r2d_y * term1_exponential);
                        double term2 = 0.5 * A_3d * realPart(u_hat_plus_r3d_y * term2_exponential);
                        double term3 = 0.5 * A_3d * realPart(u_hat_minus_r3d_y * term3_exponential);

                        double result = term1 + term2 + term3;
                        return result;
                    }


                static double addParabolicProfile(
                    double H,
                    double Ucl,
                    double y)
                {
                    return ((4.0 * Ucl / (H * H)) * y * (H - y));
                }

                };

                // Creating patch and field data
                const fvPatch& boundaryPatch = patch();
                const vectorField& Cf = boundaryPatch.Cf();
                vectorField& field = *this;

                // Getting current time
                double t = this->db().time().value();

                // To read data from dictionaries
                // dimensionedScalar nu
                // (
                //     "nu",
                //     dimViscosity,
                //     this->db().lookupObject<IOdictionary>("transportProperties").lookup("nu")
                // );


                // Read file directly
                std::ifstream inputFile("constant/polynomialRegressions");  // order of data is
                std::vector<std::vector<double>> coeffs_vector;


                std::string line;

                while (std::getline(inputFile, line)) {
                    std::stringstream ss(line);
                    double value;
                    std::vector<double> row_coeffs;
                    while (ss >> value) {
                        row_coeffs.push_back(value);
                    }
                    coeffs_vector.push_back(row_coeffs);
                }

                inputFile.close();




                // Define parameters
                double A_2d = 0.03;
                double omega_r2d = 1;
                double A_3d = 0.001;
                double beta = 2;
                double omega_r3d = 1;
                double H = 2;
                double Ucl = 1;


                // Iterating all face cells
                forAll(Cf, faceI)
                {

                    // Calculating perturbations
                    double u = local::calculate_u_tilde_component(
                        Cf[faceI].y(),
                        Cf[faceI].z(),
                        t,
                        A_2d,
                        omega_r2d,
                        A_3d,
                        beta,
                        omega_r3d,
                        coeffs_vector[0],
                        coeffs_vector[1],
                        coeffs_vector[2],
                        coeffs_vector[3]
                    );



                    double v = local::calculate_u_tilde_component(
                        Cf[faceI].y(),
                        Cf[faceI].z(),
                        t,
                        A_2d,
                        omega_r2d,
                        A_3d,
                        beta,
                        omega_r3d,
                        coeffs_vector[4],
                        coeffs_vector[5],
                        coeffs_vector[6],
                        coeffs_vector[7]
                    );

                    double w = local::calculate_u_tilde_component(
                        Cf[faceI].y(),
                        Cf[faceI].z(),
                        t,
                        A_2d,
                        omega_r2d,
                        A_3d,
                        beta,
                        omega_r3d,
                        coeffs_vector[8],
                        coeffs_vector[9],
                        coeffs_vector[10],
                        coeffs_vector[11]
                    );

                    // Adding parabolic profile
                    u += local::addParabolicProfile (H, Ucl, Cf[faceI].y());


                    // Setting boundary conditions
                    field[faceI] = vector(u,v,w);
                }
//}}} end code

    this->parent_bctype::updateCoeffs();
}


// ************************************************************************* //

