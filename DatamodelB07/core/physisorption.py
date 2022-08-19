import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import Optional


@forge_signature
class Physisorption(sdRDM.DataModel):

    """Analytical method for the determination of the specific surface area of a substance."""

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
        default="5374cd9545374920a585151e990724c1e9b3d42c"
    )
