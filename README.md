<h2>Examples</h2>
<h3>Preview</h3>

```python
from color_palette import Previewer, RGB

Previewer.preview(RGB(30, 30, 30))
```
<h3>ColorConverter</h3>

```python
from color_palette import RGB, HEX, ColorConverter

print(ColorConverter.hex_to_rgb(HEX("#dd33bd"))) # RGB(r=221, g=51, b=189)
print(ColorConverter.rgb_to_hex(RGB(156, 48, 39))) # HEX(color=#9C3027)
print(ColorConverter.mix_rgb(RGB(100, 100, 100), RGB(255, 55, 88), RGB(79, 23, 54))) # RGB(r=144, g=59, b=80)
```
