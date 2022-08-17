import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class FilmPreparation(sdRDM.DataModel):

    """Preparation of a film of the investigated polymer for carbonization."""

    m_poly_in_grams: float = Field(
        ...,
        description="Mass of the Polymer in grams",
    )

    precursor: Optional[str] = Field(
        description="Name of the precursor",
        default=None,
    )

    notice: Optional[str] = Field(
        description="Here you can write down additional notes.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="1e91f179d716d820ebebf61a497ebd8d3d0db512"
    )
