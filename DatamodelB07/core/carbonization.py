import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Carbonization(sdRDM.DataModel):
    """Heating process to burn organic substances."""

    m_f_in_grams: float = Field(..., description="Mass film")

    m_fc_in_grams: Optional[float] = Field(
        description="Mass film carbonized", default=None
    )

    loss_in_grams: Optional[float] = Field(description="Loss in grams", default=None)

    loss_in_percent: Optional[float] = Field(
        description="Loss in percent", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("carbonizationINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
