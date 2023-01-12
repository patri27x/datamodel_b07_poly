from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator
from .chemicalcompound import ChemicalCompound


@forge_signature
class Reactant(ChemicalCompound):
    """Compound that is involved in the chemical reaction, either as the product, educt, catalyst or cocatalyst.
    """

    product: Optional[str] = Field(description="...", default=None)

    educt: Optional[str] = Field(description="...", default=None)

    catalyst: Optional[str] = Field(description="...", default=None)

    cocatalyst: Optional[str] = Field(description="...", default=None)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactantINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="dac43649d84557db28e311ec3c0ab256f0b960a3"
    )
