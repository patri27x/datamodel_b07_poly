import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Stoichiometry(sdRDM.DataModel):
    """Stoichiometric information about the compound."""

    equivalents: Optional[float] = Field(
        description="Used equivalents in relation to the reference compound",
        default=None,
    )

    amount_of_substance: Optional[float] = Field(
        description="Amount of substance n in mmol", default=None
    )

    mass: Optional[float] = Field(
        description="Used mass of the compound in g", default=None
    )

    volume: Optional[float] = Field(description="Volume of the compound", default=None)

    molar_mass: Optional[float] = Field(
        description="Molar mass of the compound in g per mol", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("stoichiometryINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="b16ce082479f510e6c16837d7d78f8f72f17255f"
    )
