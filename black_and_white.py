from PIL import Image

img = Image.open("images/landscape.jpg")

img2 = img.convert("L")


#write text in the center of the image