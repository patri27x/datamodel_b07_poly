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
        default="5374cd9545374920a585151e990724c1e9b3d42c"
    )
