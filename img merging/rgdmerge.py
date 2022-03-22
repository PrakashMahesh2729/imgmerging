from PIL import Image
image = Image.open("nature-chrome-featured.jpg")
r, g, b = image.split()
image.show()
image = Image.merge("RGB", (b, g, r))
image.show()