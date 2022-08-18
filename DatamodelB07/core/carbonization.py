import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class Carbonization(sdRDM.DataModel):

    """Heating process to burn organic substances."""

    m_f_in_grams: float = Field(
        ...,
        description="Mass film",
    )

    m_fc_in_grams: Optional[float] = Field(
        description="Mass film carbonized",
        default=None,
    )

    loss_in_grams: Optional[float] = Field(
        description="Loss in grams",
        default=None,
    )

    loss_in_percent: Optional[float] = Field(
        description="Loss in percent",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e6ac54d6361bd19baa287f756522709bea86578e"
    )
