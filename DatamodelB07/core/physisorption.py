import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class Physisorption(sdRDM.DataModel):

    """..."""

    hysteresis: str = Field(
        ...,
        description="Type of hysteresis behaviour",
    )

    pore_diameter_in_nanometer: Optional[float] = Field(
        description="Self explanatory",
        default=None,
    )

    vtotal_in_cubic_centimeters_per_gram: Optional[float] = Field(
        description="Total volume",
        default=None,
    )

    ssatotal_in_square_meter_per_gram: Optional[float] = Field(
        description="Specific surface area",
        default=None,
    )

    c_constant: Optional[float] = Field(
        description="Controlling parameter",
        default=None,
    )

    wall_thickness_in_nanometer: Optional[float] = Field(
        description="Self explanatory",
        default=None,
    )

    notice: Optional[str] = Field(
        description="Here you can write down additional notes",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b7f50d16a78a14617f5b1cda63573feae5c120fd"
    )
