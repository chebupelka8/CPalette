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


<h2>Examples</h2>
<h3>Preview color</h3>

```python
from color_palette import Previewer, RGB

Previewer.preview(RGB(30, 30, 30))
```
<h3>Convert colors</h3>

```python
from color_palette import RGB, HEX, ColorConverter

print(ColorConverter.hex_to_rgb(HEX("#dd33bd"))) # RGB(r=221, g=51, b=189)
print(ColorConverter.rgb_to_hex(RGB(156, 48, 39))) # HEX(color=#9C3027)
```
<h3>Mix colors</h3>

```python
from color_palette import RGB, ColorConverter

print(ColorConverter.mix_rgb(RGB(100, 100, 100), RGB(255, 55, 88), RGB(79, 23, 54))) # RGB(r=144, g=59, b=80)
```
