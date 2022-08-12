import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from datetime import datetime
from pydantic import Field
from typing import List
from typing import Optional
from .analysis import Analysis
from .author import Author
from .personalid import PersonalID
from .synthesis import Synthesis


class Dataset(sdRDM.DataModel):

    """This is a preliminary root container for all (meta-)data."""

    id: str = Field(
        ...,
        description="Unique identifier for the dataset",
    )

    name: str = Field(
        ...,
        description="Descriptive name of the dataset",
    )

    date: datetime = Field(
        ...,
        description="Date/time when the dataset was created",
    )

    license: str = Field(
        ...,
        description="License for the dataset",
    )

    synthesis: Synthesis = Field(
        ...,
        description="...",
    )

    analysis: Optional[Analysis] = Field(
        description="...",
        default=None,
    )

    authors: List[Author] = Field(
        description="Persons who worked on the dataset",
        default_factory=ListPlus,
    )

    subjects: List[str] = Field(
        description="Research subjects covered by the datset",
        default_factory=ListPlus,
    )

    keywords: List[str] = Field(
        description="Descriptive keywords to describe the dataset",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bf57b675676ba13af4541ef0bafc065b22cff440"
    )

    def add_to_authors(
        self,
        name: str,
        affiliation: str,
        email: str,
        pid: List[PersonalID] = ListPlus(),
        phone: Optional[int] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:
            name (str): Full name of the author.
            affiliation (str): Organisation the author is affiliated with.
            email (str): Contact e-mail address of the author.
            pid (List[PersonalID]): Personal identifiers of the author.
            phone (Optional[int]): Contact phone number of the author. Defaults to None
        """

        self.authors.append(
            Author(
                name=name,
                affiliation=affiliation,
                email=email,
                pid=pid,
                phone=phone,
            )
        )
