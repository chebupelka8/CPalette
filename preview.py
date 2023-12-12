from PIL import Image
from .colors import *


class Previewer:
    """
    # Previewer

    `Methods:`
    >>> Previewer.preview(color: HEX | RGB) -> None
    """

    @staticmethod
    def preview(color: HEX | RGB) -> None:
        """>>> Previewer.preview(HEX(#303030)) # you will see image with this color"""

        Image.new("RGB", (500, 500), color.color).show()