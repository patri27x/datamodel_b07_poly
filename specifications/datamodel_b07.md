# Data model for CRC 1333 project B07

This is the perliminary data model for CRC 1333 project B07. At the current time, the data model is still under development and major changes can occur at any time. Please feel free to make changes and contribute to the project.


### Dataset

This is a preliminary root container for all (meta-)data.

- __id*__
  - Type: string
  - Description: Unique identifier for the dataset
- __name*__
  - Type: string
  - Description: Descriptive name of the dataset
- __date*__
  - Type: date
  - Description: Date/time when the dataset was created
- __authors*__
  - Type: Author
  - Multiple: True
  - Description: Persons who worked on the dataset
- __subjects*__
  - Type: string
  - Multiple: True
  - Description: Research subjects covered by the datset
- __keywords*__
  - Type: string
  - Multiple: True
  - Description: Descriptive keywords to describe the dataset
- __license*__
  - Type: string
  - Description: License for the dataset
- __synthesis*__
  - Type: Synthesis
  - Description: ...
- __analysis__
  - Type: Analysis
  - Description: ...
 

### Author

Container for information regarding persons who worked on a dataset.

- __name*__
  - Type: string
  - Description: Full name of the author
- __affiliation*__
  - Type: string
  - Description: Organisation the author is affiliated with.
- __email*__
  - Type: string
  - Description: Contact e-mail address of the author
- __phone__
  - Type: int
  - Description: Contact phone number of the author
- __pid__
  - Type: PersonalID
  - Multiple: True
  - Description: Personal identifiers of the author


### PersonalID

Container for personal identifiers related to an author

- __scheme*__
  - Type: string
  - Description: Type or scheme of personal identifier
- __identifier*__
  - Type: string
  - Description: String representation of the personal identifier


### Synthesis

All information directly related to the synthesis.

- __reaction_type__
  - Type: string
  - Description: Name of the reaction type
  - Multiple: True
- __reactants*__
  - Type: Reactant
  - Description: All reactants that are involved in the reaction
  - Multiple: True
- __solvent__
  - Type: string
  - Description: Solvent used for the reaction
- __physical_parameters*__
  - Type: PhysicalParameter
  - Description: ...
  - Multiple: True
- __apparatus__
  - Type: Apparatus
  - Description: ...
  - Multiple: True
- __processing__
  - Type: Processing
  - Description: All subsequent processing steps
  - Multiple: True
- __yield*__
  - Type: float
  - Description: Yield in percent
- __notice__
  - Type: string
  - Description: ...
- __reactant__
  - Type: Reactant
  - Description: ...

### ChemicalCompound

A chemical compound or mixtures thereof.

- __name__
  - Type: string
  - Description: If possible IUPAC name of the compound
  - Multiple: True
- __formula__
  - Type: string
  - Description: Molecular formula of the compound
- __pureness__
  - Type: float
  - Description: Pureness of the compound in percent
- __supplier__
  - Type: string
  - Description: Name of the supplier of the compound
- __stoichiometry__
  - Type: Stoichiometry
  - Description: Stoichiometric information like equivalents, mass, amount of substance, volume
- __state_of_matter__
  - Type: string
  - Description: s for solid, l for liquid and g for gaseous


### Reactant[_ChemicalCompound_]

Compound that is involved in the chemical reaction, either as the product, educt, catalyst or cocatalyst.

- __product__
  - Type: string
  - Description: ...
- __educt__
  - Type: string
  - Description: ...
- __catalyst__
  - Type: string
  - Description: ...
- __cocatalyst__
  - Type: string
  - Description: ...


### Stoichiometry

Stoichiometric information about the compound.

- __equivalents__
  - Type: float
  - Description: Used equivalents in relation to the reference compound
- __amount_of_substance__
  - Type: float
  - Description: Amount of substance n in mmol
- __mass__
  - Type: float
  - Description: Used mass of the compound in g
- __volume__
  - Type: float
  - Description: Volume of the compound
- __molar_mass__
  - Type: float
  - Description: Molar mass of the compound in g per mol

### Apparatus

Used appratuses and special equippment or techniques for the synthesis.

- __dropping_funnel__
  - Type: string
  - Description: ...
- __schlenk_technique__
  - Type: string
  - Description: ...
- __gas_injection__
  - Type: string
  - Description: ...
- __magnetic_stirring__
  - Type: string
  - Description: ...
- __vacuum__
  - Type:string
  - Description: ...


### Processing

Processing steps after the synthesis.

- __recrystallisation__
  - Type: string
  - Description: ...
- __distillation__
  - Type: string
  - Description: ...
- __film_preparation__
  - Type: FilmPreparation
  - Description: ...


### PhysicalParameter

All physical parameters that are relevant for the chemical reaction.

- __temperature__
  - Type: float
  - Description: Temperature in Kelvin
- __time__
  - Type: float
  - Description: Time in hours
- __pressure__
  - Type: float
  - Description: pressure in mbar


### Analysis

Different analyzation techniques for investigation of the products.

- __nmr__
  - Type: NMR
  - Description: ...
- __gpc__
  - Type: GPC
  - Description: ...
- __saxs__
  - Type: SAXS
  - Description: ...
- __physisorption__
  - Type: Physisorption
  - Description: ...
- __carbonization__
  - Type: Carbonization
  - Description: ...


### NMR

Nuclear magnetic resonance spectroscopy.

- __nmr_1h__
  - Type: NMR_1H
  - Description: ...

### NMR_1H

Nuclear magnetic resonance spectroscopy for detectioin of protons.

- __m_peo*__
  - Type: float
  - Description: Polyethylene oxide
- __zeropointfive_n_po__
  - Type: float
  - Description: Fraction propylene oxide
- __m_n_in_kg_per_mole__
  - Type: float
  - Description: Number average molar mass
- __hlb__
  - Type: string
  - Description: Hydrophilic to lipophilic balance



### GPC

Gel permeation chromatography.

- __mn_in_kg_per_mole*__
  - Type: float
  - Description: Number average molar mass
- __mw_in_kg_per_mole__
  - Type: float
  - Description: Mass average molar mass
- __pdi__
  - Type: float
  - Description: Polydispersity index
- __sp_in_percent__
  - Type: float
  - Description: Fractin of side products


### FilmPreparation

Preparation of a film of the investigated polymer for carbonization.

- __m_poly_in_grams*__
  - Type: float
  - Description: Mass of the Polymer in grams
- __precursor__
  - Type: string
  - Description: Name of the precursor
- __notice__
  - Type: string
  - Description: Here you can write down additional notes.
  

### Carbonization

Heating process to burn organic substances.

- __m_f_in_grams*__
  - Type: float
  - Description: Mass film
- __m_fc_in_grams__
  - Type: float
  - Description: Mass film carbonized
- __loss_in_grams__
  - Type: float
  - Description: Loss in grams
- __loss_in_percent__
  - Type: float
  - Description: Loss in percent


### SAXS

Small angle X-ray scattering.

- __ordered*__
  - Type: string
  - Description: If a crystalline structure is present
- __q10__
  - Type: float
  - Description: Scattering vector in 10 plane
- __q11__
  - Type: float
  - Description: Scattering vector in 11 plane
- __q20__
  - Type: float
  - Description: Scattering vector in 20 plane
- __q21__
  - Type: float
  - Description: Scattering vector in 21 plane
- __q10_to_q11_ratio__
  - Type: float
  - Description: Ratio of the scattering vectors 10 and 11
- __q10_to_q20_ratio__
  - Type: float
  - Description: Ratio of the scattering vectors 10 and 20
- __q10_to_q21_ratio__
  - Type: float
  - Description: Ratio of the scattering vectors 10 and 21
- __geometry__
  - Type: string
  - Description: Hexagonal, cubic ...


### Physisorption

Analytical method for the determination of the specific surface area of a substance.

- __hysteresis*__
  - Type: string
  - Description: Type of hysteresis behaviour
- __pore_diameter_in_nanometer__
  - Type: float
  - Description: Self explanatory
- __vtotal_in_cubic_centimeters_per_gram__
  - Type: float
  - Description: Total volume
- __ssatotal_in_square_meter_per_gram__
  - Type: float
  - Description: Specific surface area
- __c_constant__
  - Type: float
  - Description: Controlling parameter
- __wall_thickness_in_nanometer__
  - Type: float
  - Description: Self explanatory
- __notice__
  - Type: string
  - Description: Here you can write down additional notes
