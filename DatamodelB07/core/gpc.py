import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class GPC(sdRDM.DataModel):
    """Gel permeation chromatography."""

    mn_in_kg_per_mole: float = Field(..., description="Number average molar mass")

    mw_in_kg_per_mole: Optional[float] = Field(
        description="Mass average molar mass", default=None
    )

    pdi: Optional[float] = Field(description="Polydispersity index", default=None)

    sp_in_percent: Optional[float] = Field(
        description="Fraction of side products", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("gpcINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a15e1eec9c4bd5a5c8a66e3014f6e0c193a39a31"
    )
