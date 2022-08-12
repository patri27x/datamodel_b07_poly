import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class NMR(sdRDM.DataModel):

    """..."""

    nmr_1h: Optional[str] = Field(
        description="...",
        default=None,
    )

    m_peo: float = Field(
        ...,
        description="Polyethylene oxide",
    )

    zeropointfive_n_po: Optional[float] = Field(
        description="Fraction propylene oxide",
        default=None,
    )

    m_n_in_kg_per_mole: Optional[float] = Field(
        description="Number average molar mass",
        default=None,
    )

    hlb: Optional[str] = Field(
        description="Hydrophilic to lipophilic balance",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b7f50d16a78a14617f5b1cda63573feae5c120fd"
    )
