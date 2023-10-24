from PIL import Image
im = Image.open('0TdgibU0na.png').convert("RGB")

im.save("./0TdgibU0na1.webp", format="WebP", lossless=False)
