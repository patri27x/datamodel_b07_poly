import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field


class PersonalID(sdRDM.DataModel):

    """Container for personal identifiers related to an author"""

    scheme: str = Field(
        ...,
        description="Type or scheme of personal identifier",
    )

    identifier: str = Field(
        ...,
        description="String representation of the personal identifier",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b7f50d16a78a14617f5b1cda63573feae5c120fd"
    )
