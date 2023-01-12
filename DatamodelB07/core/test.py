from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .chemicalcompound import ChemicalCompound


@forge_signature
class Test(ChemicalCompound):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("testINDEX"),
        xml="@id",
    )
    test: Optional[str] = Field(
        description="test",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="dac43649d84557db28e311ec3c0ab256f0b960a3"
    )
