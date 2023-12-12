import re


class HEX:
    """
    # HEX
    `class HEX: -> None`
        color (str): "#FFFFFF" | "FFFFFF" | "ffffff"

        if color is not string, raises TypeError
        if color is wrong, raises ValueError
    
    >>> HEX("ffffff") -> HEX(color="#FFFFFF")
    >>> HEX("#FFFFFF").to_rgb() -> (255, 255, 255)
    >>> HEX("#3e3d3d").color -> '#3E3D3D'
    >>> HEX("#xxx") -> ValueError: Wrong color at '#xxx'
    >>> HEX("#QQQQQQ") -> ValueError: Wrong color at '#QQQQQQ'
    """

    def __init__(self, color: str) -> None:
        if color[0] == "#": self.__color = color
        else: self.__color = "#" + color

        self.__color = self.__color.upper()

        self.__verify_color(self.__color)
    
    @classmethod
    def __verify_color(cls, color: str) -> bool:
        if not isinstance(color, str): 
            raise TypeError(f"Wrong type {type(color)}")
        elif not cls.__is_hexadecimal(color): 
            raise ValueError(f"Wrong color {color}")

        return True
    
    @staticmethod
    def __is_hexadecimal(string: str) -> bool:
        return bool(re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', string))
    
    def to_rgb(self) -> tuple:
        return tuple(int(self.__color.replace("#", "")[i:i + 2], 16) for i in (0, 2, 4))

    @property
    def color(self) -> str:
        return self.__color
    
    def __repr__(self) -> str:
        return f"HEX(color={self.__color})"


class HEXA:
    """
    # HEXA
    `class HEXA: -> None`
        color (str): "#FFFFFF25" | "FFFFFF05" | "ffffff100"

        if color is not string, raises TypeError
        if color is wrong, raises ValueError
    
    >>> HEXA("ffffff30") -> HEXA(color="#FFFFFF30")
    >>> HEXA("#FFFFFF28").to_rgb() -> (255, 255, 255, 0.28)
    >>> HEXA("#3e3d3d50").color -> '#3E3D3D50'
    >>> HEXA("#xxx") -> ValueError: Wrong color at '#xxx'
    >>> HEXA("#QQQQQQ") -> ValueError: Wrong color at '#QQQQQQ'
    """

    def __init__(self, color: str) -> None:
        if color[0] == "#": self.__color = color
        else: self.__color = "#" + color

        self.__color = self.__color.upper()

        self.__verify_color(self.__color)

    @classmethod
    def __verify_color(cls, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError(f"Wrong type {type(color)}")

        if not cls.__is_hexadecimal(color):
            raise ValueError(f"Wrong color {color}")
    
    @staticmethod
    def __is_hexadecimal(string: str) -> bool:
        return bool(re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', string[:-2])) and string[-2:].isdigit() and len(string[-2:]) in (2, 3) and int(string[-2:]) <= 100
    
    def to_rgba(self) -> tuple[int, int, int, float | int]:
        res = list(int(self.__color.replace("#", "")[i:i + 2], 16) for i in (0, 2, 4))
        res.append(int(self.__color.replace("#", "")[-2:]) / 100)

        return tuple(res)
    
    @property
    def color(self) -> str:
        return self.__color

    def __repr__(self) -> str:
        return f"HEXA(color={self.__color})"


class RGB:
    """
    # RGB
    `class RGB: -> None`
        r (int): 0 >= red <= 255 // red color
        g (int): 0 >= green <= 255 // green color
        b (int): 0 >= blue <= 255 // blue color

        if color less 0 or more 255, raises ValueError
    
    >>> RGB(0, 0, 0) -> RGB(r=0, g=0, b=0)
    >>> RGB(255, 255, 255).to_hex(upper=True, hashtag=False) -> FFFFFF
    >>> RGB(30, 30, 30).color -> (30, 30, 30)
    >>> RGB(256, -2, 400) -> ValueError: Wrong color at (r=256, g=-2, b=400)
    >>> RGB(100, 100, 100) + RGB(30, 30, 30) -> RGB(r=65, g=65, b=65) # WARNING!!! Don't use this if you have more than 2 color
    
    >>> ColorConverter.mix_rgb(RGB(100, 100, 100), RGB(30, 30, 30), RGB(255, 255, 255)) -> RGB(r=128, g=128, b=128) # If you have more than 2 colors, use this.
    """

    def __init__(self, r: int, g: int, b: int) -> None:
        self.__red = r
        self.__green = g
        self.__blue = b

        self.__verify_color([self.__red, self.__green, self.__blue])
    
    @classmethod
    def __check_channel(cls, channel: int) -> bool:
        if channel > 255 or channel < 0: return False
        elif not isinstance(channel, int): return False
        else: return True

    @classmethod
    def __verify_color(cls, color: list | tuple) -> None | bool:
        if not all(map(lambda cl: cls.__check_channel(cl), color)): 
            raise ValueError(f"Wrong color at (r={color[0]}, g={color[1]}, b={color[2]})")
        
        return True
    
    def to_hex(self, upper: bool = True, hashtag: bool = True) -> str:
        res = "{0:02x}{1:02x}{2:02x}".format(self.__red, self.__green, self.__blue)
        
        if upper: res = res.upper()
        if hashtag: res = "#" + res

        return res

    @property
    def color(self) -> tuple[int, int, int]:
        return (self.__red, self.__green, self.__blue)

    def __repr__(self) -> str:
        return f"RGB(r={self.__red}, g={self.__green}, b={self.__blue})"

    def __add__(self, other):
        if not isinstance(other, RGB):
            raise TypeError(f"Wrong type at {type(other)}")
        
        return RGB(
            (self.color[0] + other.color[0]) // 2, 
            (self.color[1] + other.color[1]) // 2, 
            (self.color[2] + other.color[2]) // 2
        )


class RGBA:
    """
    # RGBA
    `class RGBA: -> None`
        r (int): 0 >= red <= 255 // red color
        g (int): 0 >= green <= 255 // green color
        b (int): 0 >= blue <= 255 // blue color
        alpha (int | float): 0 >= alpha <= 1 // alpha channel

        if color less 0 or more 255, raises ValueError
        if alpha channel less 0 or more 1, raises ValueError
    
    >>> RGBA(0, 0, 0, 0.5) -> RGBA(r=0, g=0, b=0, alpha=0.5)
    >>> RGBA(30, 30, 30, 0.2).color -> (30, 30, 30, 0.2)
    >>> RGBA(256, -2, 400, 1.1) -> ValueError: Wrong color at (r=256, g=-2, b=400, alpha=1.1)
    >>> RGBA(43, 128, 85, 0.8).to_hex() -> "#2B805580"
    >>> RGBA(100, 100, 100, 0.3) + RGBA(30, 30, 30, 0.8) -> RGBA(r=65, g=65, b=65, alpha=0.55) # WARNING!!! Don't use this if you have more than 2 color
    
    >>> ColorConverter.mix_rgb(RGBA(100, 100, 100, 0.2), RGBA(30, 30, 30, 0.4), RGBA(255, 255, 255, 0.65)) -> RGBA(r=128, g=128, b=128, alpha=0.42) # If you have more than 2 colors, use this.
    """

    def __init__(self, r: int, g: int, b: int, alpha: int | float) -> None:
        self.__red = r
        self.__green = g
        self.__blue = b
        self.__alpha = alpha

        self.__verify_color([self.__red, self.__green, self.__blue, self.__alpha])
    
    @classmethod
    def __check_channel(cls, channel: int) -> bool:
        if not isinstance(channel, int): return False
        elif channel > 255 or channel < 0: return False
        else: return True

    @classmethod
    def __check_alpha_channel(cls, channel: int) -> bool:
        if not isinstance(channel, (int, float)): return False
        elif channel > 1 or channel < 0: return False
        else: return True 
    
    @classmethod
    def __verify_color(cls, color: list | tuple) -> bool:
        if not cls.__check_alpha_channel(color[-1]) or not all(map(lambda cl: cls.__check_channel(cl), color[:-1])):
            raise ValueError(f"Wrong color at (r={color[0]}, g={color[1]}, b={color[2]}, alpha={color[3]})")
        
    def __repr__(self) -> str:
        return f"RGBA(r={self.__red}, g={self.__green}, b={self.__blue}, alpha={self.__alpha})"

    @property
    def color(self) -> tuple[int, int, int, int | float]:
        return (self.__red, self.__green, self.__blue, self.__alpha)
    
    def to_hex(self, upper: bool = True, hashtag: bool = True) -> str:
        res = f"{self.__red:02x}{self.__green:02x}{self.__blue:02x}{int(self.__alpha * 100):02}"

        if upper: res = res.upper()
        if hashtag: res = "#" + res

        return res
    
    def __add__(self, other):
        if not isinstance(other, RGBA):
            raise TypeError(f"Wrong type for {type(other)}")
        
        return RGBA(
            (self.__red + other.color[0]) // 2,
            (self.__green + other.color[1]) // 2,
            (self.__blue + other.color[2]) // 2,
            round((self.__alpha + other.color[3]) / 2, 2)
        )