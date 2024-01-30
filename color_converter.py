from .colors import *


class ColorConverter:

    @staticmethod
    def rgb_to_hex(rgb: RGB) -> HEX:
        return HEX(rgb.to_hex())
    
    @staticmethod
    def hex_to_rgb(hex: HEX) -> RGB:
        return RGB(*hex.to_rgb())
    
    @staticmethod
    def rgba_to_hexa(rgba: RGBA) -> HEXA:
        return None
    
    @staticmethod
    def hexa_to_rgba(hexa: HEXA) -> RGBA:
        return None
    
    @staticmethod
    def mix_rgb(*colors: RGB) -> RGB:
        count = len(colors)
        result = [0, 0, 0]

        for rgb in colors: result = [result[0] + rgb.color[0], result[1] + rgb.color[1], result[2] + rgb.color[2]]

        return RGB(*map(lambda color: color // count, result))
    
    @staticmethod
    def mix_rgba(*colors: RGBA) -> RGBA:
        count = len(colors)
        result = [0, 0, 0, 0]

        for rgb in colors: result = [result[0] + rgb.color[0], result[1] + rgb.color[1], result[2] + rgb.color[2], result[3] + rgb.color[3]]

        return RGBA(*map(lambda color: color // count, result[:-1]), round(result[-1] / count, 2))

        