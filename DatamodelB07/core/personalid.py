import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class PersonalID(sdRDM.DataModel):
    """Container for personal identifiers related to an author"""

    scheme: str = Field(..., description="Type or scheme of personal identifier")

    identifier: str = Field(
        ..., description="String representation of the personal identifier"
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("personalidINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
