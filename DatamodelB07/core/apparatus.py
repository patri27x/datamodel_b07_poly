import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class Apparatus(sdRDM.DataModel):

    """Used appratuses and special equippment or techniques for the synthesis."""

    dropping_funnel: Optional[str] = Field(
        description="...",
        default=None,
    )

    schlenk_technique: Optional[str] = Field(
        description="...",
        default=None,
    )

    gas_injection: Optional[str] = Field(
        description="...",
        default=None,
    )

    magnetic_stirring: Optional[str] = Field(
        description="...",
        default=None,
    )

    vacuum: Optional[str] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="1e91f179d716d820ebebf61a497ebd8d3d0db512"
    )
