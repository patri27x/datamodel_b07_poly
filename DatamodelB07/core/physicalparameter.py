import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class PhysicalParameter(sdRDM.DataModel):
    """All physical parameters that are relevant for the chemical reaction."""

    temperature: Optional[float] = Field(
        description="Temperature in Kelvin", default=None
    )

    time: Optional[float] = Field(description="Time in hours", default=None)

    pressure: Optional[float] = Field(description="pressure in mbar", default=None)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("physicalparameterINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a15e1eec9c4bd5a5c8a66e3014f6e0c193a39a31"
    )
