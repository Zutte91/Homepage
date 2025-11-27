from PIL import Image
from collections import Counter
import os

img_path = os.path.join(os.path.dirname(__file__), '..', 'media', 'EZit LOGO.jpg')

if not os.path.exists(img_path):
    print('ERROR: logo not found at', img_path)
    raise SystemExit(1)

img = Image.open(img_path).convert('RGBA')
# Resize to reduce colors
img_small = img.resize((120, 120))

# Get colors, ignore fully transparent
pixels = [px for px in img_small.getdata() if px[3] > 0]

# Convert to RGB tuples
rgb_pixels = [(r, g, b) for (r, g, b, a) in pixels]

counter = Counter(rgb_pixels)
most_common = counter.most_common(10)

# Function to convert to hex
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

# Filter out near-white and near-black
filtered = []
for (rgb, count) in most_common:
    r,g,b = rgb
    lum = (0.2126*r + 0.7152*g + 0.0722*b)
    if lum > 245:  # near white
        continue
    if lum < 10:   # near black
        continue
    filtered.append((rgb, count))
    if len(filtered) >= 5:
        break

if not filtered:
    # fallback to top colors
    filtered = most_common[:3]

hex_colors = [rgb_to_hex(rgb) for (rgb,count) in filtered]

# Choose primary, accent, dark heuristically
primary = hex_colors[0] if len(hex_colors) > 0 else '#1e40af'
accent = hex_colors[1] if len(hex_colors) > 1 else '#3b82f6'
# dark: choose a darker variant of primary if available

# compute darker variant
def darken(hexc, amount=0.25):
    hexc = hexc = hexc.lstrip('#')
    r = int(hexc[0:2],16)
    g = int(hexc[2:4],16)
    b = int(hexc[4:6],16)
    r = max(0, int(r*(1-amount)))
    g = max(0, int(g*(1-amount)))
    b = max(0, int(b*(1-amount)))
    return '#%02x%02x%02x' % (r,g,b)

# choose dark as a darker primary or third color
if len(hex_colors) > 2:
    dark = hex_colors[2]
else:
    dark = darken(primary, 0.25)

print('PRIMARY', primary)
print('ACCENT', accent)
print('DARK', dark)
print('\n# All detected (filtered) colors:')
for h in hex_colors:
    print(h)
