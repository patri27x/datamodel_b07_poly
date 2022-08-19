import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import Optional
from .carbonization import Carbonization
from .gpc import GPC
from .nmr import NMR
from .physisorption import Physisorption
from .saxs import SAXS


@forge_signature
class Analysis(sdRDM.DataModel):

    """Different analyzation techniques for investigation of the products."""

    nmr: Optional[NMR] = Field(
        description="...",
        default_factory=NMR,
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
        default="5374cd9545374920a585151e990724c1e9b3d42c"
    )
