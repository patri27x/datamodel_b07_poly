from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import Optional
from .chemicalcompound import ChemicalCompound


@forge_signature
class Reactant(ChemicalCompound):

    """Compound that is involved in the chemical reaction, either as the product, educt, catalyst or cocatalyst."""

    product: Optional[str] = Field(
        description="...",
        default=None,
    )

    educt: Optional[str] = Field(
        description="...",
        default=None,
    )

    catalyst: Optional[str] = Field(
        description="...",
        default=None,
    )

    cocatalyst: Optional[str] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
