import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator

from .carbonization import Carbonization
from .gpc import GPC
from .nmr import NMR
from .physisorption import Physisorption
from .saxs import SAXS


@forge_signature
class Analysis(sdRDM.DataModel):
    """Different analyzation techniques for investigation of the products."""

    nmr: Optional[NMR] = Field(description="...", default_factory=NMR)

    gpc: Optional[GPC] = Field(description="...", default=None)

    saxs: Optional[SAXS] = Field(description="...", default=None)

    physisorption: Optional[Physisorption] = Field(description="...", default=None)

    carbonization: Optional[Carbonization] = Field(description="...", default=None)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
