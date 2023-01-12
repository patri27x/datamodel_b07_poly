import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Apparatus(sdRDM.DataModel):
    """Used appratuses and special equippment or techniques for the synthesis."""

    dropping_funnel: Optional[str] = Field(description="...", default=None)

    schlenk_technique: Optional[str] = Field(description="...", default=None)

    gas_injection: Optional[str] = Field(description="...", default=None)

    magnetic_stirring: Optional[str] = Field(description="...", default=None)

    vacuum: Optional[str] = Field(description="...", default=None)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("apparatusINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="dac43649d84557db28e311ec3c0ab256f0b960a3"
    )
