import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class GPC(sdRDM.DataModel):

    """Gel permeation chromatography."""

    mn_in_kg_per_mole: float = Field(
        ...,
        description="Number average molar mass",
    )

    mw_in_kg_per_mole: Optional[float] = Field(
        description="Mass average molar mass",
        default=None,
    )

    pdi: Optional[float] = Field(
        description="Polydispersity index",
        default=None,
    )

    sp_in_percent: Optional[float] = Field(
        description="Fraction of side products",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="1e91f179d716d820ebebf61a497ebd8d3d0db512"
    )
