import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class NMREINSH(sdRDM.DataModel):
    """Nuclear magnetic resonance spectroscopy for detection of protons."""

    m_peo: float = Field(..., description="Polyethylene oxide")

    zeropointfive_n_po: Optional[float] = Field(
        description="Fraction propylene oxide", default=None
    )

    m_n_in_kg_per_mole: Optional[float] = Field(
        description="Number average molar mass", default=None
    )

    hlb: Optional[str] = Field(
        description="Hydrophilic to lipophilic balance", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("nmreinshINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="9137756c19679e9e346a5ebe69b58357546531b9"
    )
