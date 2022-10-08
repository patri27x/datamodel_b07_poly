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
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
