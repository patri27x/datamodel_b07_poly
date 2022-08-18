import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class SAXS(sdRDM.DataModel):

    """Small angle X-ray scattering."""

    ordered: str = Field(
        ...,
        description="If a crystalline structure is present",
    )

    geometry: Optional[str] = Field(
        description="Hexagonal, cubic ...",
        default=None,
    )

    q10: Optional[float] = Field(
        description="Scattering vector in 10 plane",
        default=None,
    )

    q11: Optional[float] = Field(
        description="Scattering vector in 11 plane",
        default=None,
    )

    q20: Optional[float] = Field(
        description="Scattering vector in 20 plane",
        default=None,
    )

    q21: Optional[float] = Field(
        description="Scattering vector in 21 plane",
        default=None,
    )

    q10_to_q11_ratio: Optional[float] = Field(
        description="Ratio of the scattering vectors 10 and 11",
        default=None,
    )

    q10_to_q20_ratio: Optional[float] = Field(
        description="Ratio of the scattering vectors 10 and 20",
        default=None,
    )

    q10_to_q21_ratio: Optional[float] = Field(
        description="Ratio of the scattering vectors 10 and 21",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e6ac54d6361bd19baa287f756522709bea86578e"
    )
