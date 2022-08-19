import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import List
from typing import Optional
from .stoichiometry import Stoichiometry


@forge_signature
class ChemicalCompound(sdRDM.DataModel):

    """A chemical compound or mixtures thereof."""

    name: List[str] = Field(
        description="If possible IUPAC name of the compound",
        default_factory=ListPlus,
    )

    formula: Optional[str] = Field(
        description="Molecular formula of the compound",
        default=None,
    )

    pureness: Optional[float] = Field(
        description="Pureness of the compound in percent",
        default=None,
    )

    supplier: Optional[str] = Field(
        description="Name of the supplier of the compound",
        default=None,
    )

    stoichiometry: Optional[Stoichiometry] = Field(
        description="Stoichiometric information like equivalents, mass, amount of substance, volume",
        default_factory=Stoichiometry,
    )

    state_of_matter: Optional[str] = Field(
        description="s for solid, l for liquid and g for gaseous",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
