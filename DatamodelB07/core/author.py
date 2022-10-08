import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator

from .personalid import PersonalID


@forge_signature
class Author(sdRDM.DataModel):
    """Container for information regarding persons who worked on a dataset."""

    name: str = Field(..., description="Full name of the author")

    affiliation: str = Field(
        ..., description="Organisation the author is affiliated with."
    )

    email: str = Field(..., description="Contact e-mail address of the author")

    phone: Optional[int] = Field(
        description="Contact phone number of the author", default=None
    )

    pid: List[PersonalID] = Field(
        description="Personal identifiers of the author", default_factory=ListPlus
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )

    def add_to_pid(self, scheme: str, identifier: str) -> None:
        """
        Adds an instance of 'PersonalID' to the attribute 'pid'.

        Args:


            scheme (str): Type or scheme of personal identifier.


            identifier (str): String representation of the personal identifier.
        """
        pid = [PersonalID(scheme=scheme, identifier=identifier)]
        self.pid = self.pid + pid
