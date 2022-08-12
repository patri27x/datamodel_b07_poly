import sdRDM

 
from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import List
from typing import Optional
from .apparatus import Apparatus
from .chemicalcompound import ChemicalCompound
from .filmpreparation import FilmPreparation
from .physicalparameter import PhysicalParameter
from .processing import Processing
from .reactant import Reactant
class Synthesis(sdRDM.DataModel):

                
    """...description...
"""

    physical_parameters: List[PhysicalParameter] = Field(    
    description="...",    default_factory=ListPlus,    )

    apparatus: List[Apparatus] = Field(    
    description="...",    default_factory=ListPlus,    )

    yield: float = Field(
    ...,    description="Yield in percent",    )

    notice: Optional[str] = Field(    
    description="...",    default=None,    )

    reactant: Optional[Reactant] = Field(    
    description="...",    default=None,    )

    reaction_type: List[str] = Field(    
    description="Name of the reaction type",    default_factory=ListPlus,    )

    reactants: List[Reactant] = Field(    
    description="All reactants that are involved in the reaction",    default_factory=ListPlus,    )

    solvent: Optional[str] = Field(    
    description="Solvent used for the reaction",    default=None,    )

    processing: List[Processing] = Field(    
    description="All subsequent processing steps",    default_factory=ListPlus,    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/FAIRChemistry/datamodel_b07.git")
    __commit__: Optional[str] = PrivateAttr(default="b7f50d16a78a14617f5b1cda63573feae5c120fd")
    
    def add_to_reactants(
        self,
        product: Optional[str] = None ,
        educt: Optional[str] = None ,
        catalyst: Optional[str] = None ,
        cocatalyst: Optional[str] = None ,
    ) -> None:
        """
        Adds an instance of 'Reactant' to the attribute 'reactants'.

        Args:
            product (Optional[str]): .. Defaults to None
            educt (Optional[str]): .. Defaults to None
            catalyst (Optional[str]): .. Defaults to None
            cocatalyst (Optional[str]): .. Defaults to None
        """

        self.reactants.append(
            Reactant(
                product=product,
                educt=educt,
                catalyst=catalyst,
                cocatalyst=cocatalyst,
            )
        )
    def add_to_physical_parameters(
        self,
        temperature: Optional[float] = None ,
        time: Optional[float] = None ,
        pressure: Optional[float] = None ,
    ) -> None:
        """
        Adds an instance of 'PhysicalParameter' to the attribute 'physical_parameters'.

        Args:
            temperature (Optional[float]): Temperature in Kelvin. Defaults to None
            time (Optional[float]): Time in hours. Defaults to None
            pressure (Optional[float]): pressure in mbar. Defaults to None
        """

        self.physical_parameters.append(
            PhysicalParameter(
                temperature=temperature,
                time=time,
                pressure=pressure,
            )
        )
    def add_to_apparatus(
        self,
        field: Optional[str] = None ,
    ) -> None:
        """
        Adds an instance of 'Apparatus' to the attribute 'apparatus'.

        Args:
            field (Optional[str]): .. Defaults to None
        """

        self.apparatus.append(
            Apparatus(
                field=field,
            )
        )
    def add_to_processing(
        self,
        field: Optional[str] = None ,
        film_preparation: Optional[FilmPreparation] = None ,
    ) -> None:
        """
        Adds an instance of 'Processing' to the attribute 'processing'.

        Args:
            field (Optional[str]): .. Defaults to None
            film_preparation (Optional[FilmPreparation]): .. Defaults to None
        """

        self.processing.append(
            Processing(
                field=field,
                film_preparation=film_preparation,
            )
        )