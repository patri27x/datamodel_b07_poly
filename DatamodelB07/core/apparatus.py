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
        default="5374cd9545374920a585151e990724c1e9b3d42c"
    )
