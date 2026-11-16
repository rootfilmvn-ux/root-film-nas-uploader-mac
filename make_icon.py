import os, subprocess
from PIL import Image, ImageDraw, ImageFont

size = 1024
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rounded_rectangle([40, 40, 984, 984], radius=216, fill=(17, 24, 39, 255), outline=(56, 189, 248, 255), width=32)
draw.ellipse([136, 136, 888, 888], outline=(30, 58, 138, 255), width=16)
draw.polygon([(512, 192), (736, 456), (592, 456), (592, 688), (432, 688), (432, 456), (288, 456)], fill=(56, 189, 248, 255))
draw.rounded_rectangle([224, 728, 800, 888], radius=40, fill=(245, 158, 11, 255))
try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 108)
except Exception:
    font = ImageFont.load_default()
bbox = draw.textbbox((0, 0), "NAS UP", font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text(((size - tw) / 2, 728 + (160 - th) / 2 - 12), "NAS UP", fill=(15, 18, 24, 255), font=font)

os.makedirs("app.iconset", exist_ok=True)
for px, fname in [(16,"icon_16x16.png"),(32,"icon_16x16@2x.png"),(32,"icon_32x32.png"),(64,"icon_32x32@2x.png"),(128,"icon_128x128.png"),(256,"icon_128x128@2x.png"),(256,"icon_256x256.png"),(512,"icon_256x256@2x.png"),(512,"icon_512x512.png"),(1024,"icon_512x512@2x.png")]:
    img.resize((px, px), Image.Resampling.LANCZOS).save(os.path.join("app.iconset", fname))
subprocess.run(["iconutil", "-c", "icns", "app.iconset", "-o", "app_icon.icns"], check=False)