import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class FilmPreparation(sdRDM.DataModel):
    """Preparation of a film of the investigated polymer for carbonization."""

    m_poly_in_grams: float = Field(..., description="Mass of the Polymer in grams")

    precursor: Optional[str] = Field(description="Name of the precursor", default=None)

    notice: Optional[str] = Field(
        description="Here you can write down additional notes.", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("filmpreparationINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="dac43649d84557db28e311ec3c0ab256f0b960a3"
    )
