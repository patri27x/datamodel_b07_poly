import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


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
        default="1e91f179d716d820ebebf61a497ebd8d3d0db512"
    )
