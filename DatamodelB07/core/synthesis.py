import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import List
from typing import Optional
from .apparatus import Apparatus
from .chemicalcompound import ChemicalCompound
from .filmpreparation import FilmPreparation
from .physicalparameter import PhysicalParameter
from .processing import Processing
from .reactant import Reactant


@forge_signature
class Synthesis(sdRDM.DataModel):

    """All information directly related to the synthesis."""

    physical_parameters: List[PhysicalParameter] = Field(
        description="...",
        default_factory=ListPlus,
    )

    apparatus: List[Apparatus] = Field(
        description="...",
        default_factory=ListPlus,
    )

    yield_: float = Field(
        ...,
        description="Yield in percent",
        alias="yield",
    )

    notice: Optional[str] = Field(
        description="...",
        default=None,
    )

    reactant: Optional[Reactant] = Field(
        description="...",
        default_factory=Reactant,
    )

    reaction_type: List[str] = Field(
        description="Name of the reaction type",
        default_factory=ListPlus,
    )

    reactants: List[Reactant] = Field(
        description="All reactants that are involved in the reaction",
        default_factory=ListPlus,
    )

    solvent: Optional[str] = Field(
        description="Solvent used for the reaction",
        default=None,
    )

    processing: List[Processing] = Field(
        description="All subsequent processing steps",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="5374cd9545374920a585151e990724c1e9b3d42c"
    )

    def add_to_reactants(
        self,
        product: Optional[str] = None,
        educt: Optional[str] = None,
        catalyst: Optional[str] = None,
        cocatalyst: Optional[str] = None,
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
        temperature: Optional[float] = None,
        time: Optional[float] = None,
        pressure: Optional[float] = None,
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
        dropping_funnel: Optional[str] = None,
        schlenk_technique: Optional[str] = None,
        gas_injection: Optional[str] = None,
        magnetic_stirring: Optional[str] = None,
        vacuum: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Apparatus' to the attribute 'apparatus'.

        Args:
            dropping_funnel (Optional[str]): .. Defaults to None
            schlenk_technique (Optional[str]): .. Defaults to None
            gas_injection (Optional[str]): .. Defaults to None
            magnetic_stirring (Optional[str]): .. Defaults to None
            vacuum (Optional[str]): .. Defaults to None
        """

        self.apparatus.append(
            Apparatus(
                dropping_funnel=dropping_funnel,
                schlenk_technique=schlenk_technique,
                gas_injection=gas_injection,
                magnetic_stirring=magnetic_stirring,
                vacuum=vacuum,
            )
        )

    def add_to_processing(
        self,
        recrystallisation: Optional[str] = None,
        distillation: Optional[str] = None,
        film_preparation: Optional[FilmPreparation] = None,
    ) -> None:
        """
        Adds an instance of 'Processing' to the attribute 'processing'.

        Args:
            recrystallisation (Optional[str]): .. Defaults to None
            distillation (Optional[str]): .. Defaults to None
            film_preparation (Optional[FilmPreparation]): .. Defaults to None
        """

        self.processing.append(
            Processing(
                recrystallisation=recrystallisation,
                distillation=distillation,
                film_preparation=film_preparation,
            )
        )
