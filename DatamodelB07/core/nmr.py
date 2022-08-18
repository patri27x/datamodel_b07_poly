import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional
from .nmreinsh import NMREINSH


class NMR(sdRDM.DataModel):

    """Nuclear magnetic resonance spectroscopy."""

    nmr_1h: Optional[NMREINSH] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e6ac54d6361bd19baa287f756522709bea86578e"
    )
