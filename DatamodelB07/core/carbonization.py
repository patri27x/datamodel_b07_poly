import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class Carbonization(sdRDM.DataModel):

    """..."""

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
        default="bf57b675676ba13af4541ef0bafc065b22cff440"
    )
