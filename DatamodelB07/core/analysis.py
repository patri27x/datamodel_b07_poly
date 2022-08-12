import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional
from .carbonization import Carbonization
from .gpc import GPC
from .nmr import NMR
from .physisorption import Physisorption
from .saxs import SAXS


class Analysis(sdRDM.DataModel):

    """..."""

    nmr: Optional[NMR] = Field(
        description="...",
        default=None,
    )

    gpc: Optional[GPC] = Field(
        description="...",
        default=None,
    )

    saxs: Optional[SAXS] = Field(
        description="...",
        default=None,
    )

    physisorption: Optional[Physisorption] = Field(
        description="...",
        default=None,
    )

    carbonization: Optional[Carbonization] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b7f50d16a78a14617f5b1cda63573feae5c120fd"
    )
