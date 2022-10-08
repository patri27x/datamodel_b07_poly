import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class SAXS(sdRDM.DataModel):
    """Small angle X-ray scattering."""

    ordered: str = Field(..., description="If a crystalline structure is present")

    geometry: Optional[str] = Field(description="Hexagonal, cubic ...", default=None)

    q10: Optional[float] = Field(
        description="Scattering vector in 10 plane", default=None
    )

    q11: Optional[float] = Field(
        description="Scattering vector in 11 plane", default=None
    )

    q20: Optional[float] = Field(
        description="Scattering vector in 20 plane", default=None
    )

    q21: Optional[float] = Field(
        description="Scattering vector in 21 plane", default=None
    )

    q10_to_q11_ratio: Optional[float] = Field(
        description="Ratio of the scattering vectors 10 and 11", default=None
    )

    q10_to_q20_ratio: Optional[float] = Field(
        description="Ratio of the scattering vectors 10 and 20", default=None
    )

    q10_to_q21_ratio: Optional[float] = Field(
        description="Ratio of the scattering vectors 10 and 21", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("saxsINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
