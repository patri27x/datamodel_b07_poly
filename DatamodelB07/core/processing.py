import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional
from .filmpreparation import FilmPreparation


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
        default="1e91f179d716d820ebebf61a497ebd8d3d0db512"
    )
