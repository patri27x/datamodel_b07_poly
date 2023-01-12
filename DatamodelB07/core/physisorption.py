import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Physisorption(sdRDM.DataModel):
    """Analytical method for the determination of the specific surface area of a substance.
    """

    hysteresis: str = Field(..., description="Type of hysteresis behaviour")

    pore_diameter_in_nanometer: Optional[float] = Field(
        description="Self explanatory", default=None
    )

    vtotal_in_cubic_centimeters_per_gram: Optional[float] = Field(
        description="Total volume", default=None
    )

    ssatotal_in_square_meter_per_gram: Optional[float] = Field(
        description="Specific surface area", default=None
    )

    c_constant: Optional[float] = Field(
        description="Controlling parameter", default=None
    )

    wall_thickness_in_nanometer: Optional[float] = Field(
        description="Self explanatory", default=None
    )

    notice: Optional[str] = Field(
        description="Here you can write down additional notes", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("physisorptionINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a15e1eec9c4bd5a5c8a66e3014f6e0c193a39a31"
    )
