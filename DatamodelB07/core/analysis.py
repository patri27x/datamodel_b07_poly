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

    """Different analyzation techniques for investigation of the products."""

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
        default="1e91f179d716d820ebebf61a497ebd8d3d0db512"
    )
