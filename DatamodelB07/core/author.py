import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import List
from typing import Optional
from .personalid import PersonalID


class Author(sdRDM.DataModel):

    """Container for information regarding persons who worked on a dataset."""

    name: str = Field(
        ...,
        description="Full name of the author",
    )

    affiliation: str = Field(
        ...,
        description="Organisation the author is affiliated with.",
    )

    email: str = Field(
        ...,
        description="Contact e-mail address of the author",
    )

    phone: Optional[int] = Field(
        description="Contact phone number of the author",
        default=None,
    )

    pid: List[PersonalID] = Field(
        description="Personal identifiers of the author",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bf57b675676ba13af4541ef0bafc065b22cff440"
    )

    def add_to_pid(
        self,
        scheme: str,
        identifier: str,
    ) -> None:
        """
        Adds an instance of 'PersonalID' to the attribute 'pid'.

        Args:
            scheme (str): Type or scheme of personal identifier.
            identifier (str): String representation of the personal identifier.
        """

        self.pid.append(
            PersonalID(
                scheme=scheme,
                identifier=identifier,
            )
        )
