from .analysis import Analysis
from .apparatus import Apparatus
from .author import Author
from .carbonization import Carbonization
from .chemicalcompound import ChemicalCompound
from .dataset import Dataset
from .filmpreparation import FilmPreparation
from .gpc import GPC
from .nmr import NMR
from .personalid import PersonalID
from .physicalparameter import PhysicalParameter
from .physisorption import Physisorption
from .processing import Processing
from .reactant import Reactant
from .saxs import SAXS
from .stoichiometry import Stoichiometry
from .synthesis import Synthesis

__doc__ = "This is the perliminary data model for CRC 1333 project B07. At the current time, the data model is still under development and major changes can occur at any time. Please feel free to make changes and contribute to the project."

__all__ = [
    "Analysis",
    "Apparatus",
    "Author",
    "Carbonization",
    "ChemicalCompound",
    "Dataset",
    "FilmPreparation",
    "GPC",
    "NMR",
    "PersonalID",
    "PhysicalParameter",
    "Physisorption",
    "Processing",
    "Reactant",
    "SAXS",
    "Stoichiometry",
    "Synthesis",
]
