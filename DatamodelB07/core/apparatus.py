import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic import Field
from typing import Optional


@forge_signature
class Apparatus(sdRDM.DataModel):

    """Used appratuses and special equippment or techniques for the synthesis."""

    dropping_funnel: Optional[str] = Field(
        description="...",
        default=None,
    )

    schlenk_technique: Optional[str] = Field(
        description="...",
        default=None,
    )

    gas_injection: Optional[str] = Field(
        description="...",
        default=None,
    )

    magnetic_stirring: Optional[str] = Field(
        description="...",
        default=None,
    )

    vacuum: Optional[str] = Field(
        description="...",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b07.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8ca837b868a3820116c4117e22632b432a667f51"
    )
