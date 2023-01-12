import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from datetime import datetime
from sdRDM.base.utils import forge_signature, IDGenerator
from .analysis import Analysis
from .author import Author
from .personalid import PersonalID
from .synthesis import Synthesis


@forge_signature
class Dataset(sdRDM.DataModel):
    """This is a preliminary root container for all (meta-)data."""

    name: str = Field(..., description="Descriptive name of the dataset")

    date: datetime = Field(..., description="Date/time when the dataset was created")

    license: str = Field(..., description="License for the dataset")

    authors: List[Author] = Field(
        description="Persons who worked on the dataset", default_factory=ListPlus
    )

    subjects: List[str] = Field(
        description="Research subjects covered by the datset", default_factory=ListPlus
    )

    keywords: List[str] = Field(
        description="Descriptive keywords to describe the dataset",
        default_factory=ListPlus,
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    synthesis: Synthesis = Field(description="...", default=None)

    analysis: Optional[Analysis] = Field(description="...", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a15e1eec9c4bd5a5c8a66e3014f6e0c193a39a31"
    )

    def add_to_authors(
        self,
        name: str,
        affiliation: str,
        email: str,
        pid: List[PersonalID],
        phone: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'authors'.

        Args:


            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.


            name (str): Full name of the author.


            affiliation (str): Organisation the author is affiliated with.


            email (str): Contact e-mail address of the author.


            pid (List[PersonalID]): Personal identifiers of the author.


            phone (Optional[int]): Contact phone number of the author. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
            "email": email,
            "pid": pid,
            "phone": phone,
        }
        if id is not None:
            params["id"] = id
        authors = [Author(**params)]
        self.authors = self.authors + authors
