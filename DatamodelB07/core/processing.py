import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import Optional
from .filmpreparation import FilmPreparation


@forge_signature
class Processing(sdRDM.DataModel):

    """Processing steps after the synthesis."""

    recrystallisation: Optional[str] = Field(
        description="...",
        default=None,
    )

    distillation: Optional[str] = Field(
        description="...",
        default=None,
    )

    film_preparation: Optional[FilmPreparation] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
