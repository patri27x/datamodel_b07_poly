import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator
from .filmpreparation import FilmPreparation


@forge_signature
class Processing(sdRDM.DataModel):
    """Processing steps after the synthesis."""

    recrystallisation: Optional[str] = Field(description="...", default=None)

    distillation: Optional[str] = Field(description="...", default=None)

    film_preparation: Optional[FilmPreparation] = Field(description="...", default=None)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("processingINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a15e1eec9c4bd5a5c8a66e3014f6e0c193a39a31"
    )
