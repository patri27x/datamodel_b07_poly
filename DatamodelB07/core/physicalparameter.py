import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import Optional


@forge_signature
class PhysicalParameter(sdRDM.DataModel):

    """All physical parameters that are relevant for the chemical reaction."""

    temperature: Optional[float] = Field(
        description="Temperature in Kelvin",
        default=None,
    )

    time: Optional[float] = Field(
        description="Time in hours",
        default=None,
    )

    pressure: Optional[float] = Field(
        description="pressure in mbar",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="5374cd9545374920a585151e990724c1e9b3d42c"
    )
