import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator
from .nmreinsh import NMREINSH


@forge_signature
class NMR(sdRDM.DataModel):
    """Nuclear magnetic resonance spectroscopy."""

    nmr_1h: Optional[NMREINSH] = Field(description="...", default=None)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("nmrINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="dac43649d84557db28e311ec3c0ab256f0b960a3"
    )
