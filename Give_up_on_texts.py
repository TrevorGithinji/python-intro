from PIL import Image, ImageDraw, ImageFont

# Create an image
image = Image.open("images/landscape.jpg")
#image = Image.new('RGB', (300, 100), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Define the text and font
text = "Hello, World!"
font = ImageFont.load_default()  # Or you can load your own font here

# Get the bounding box of the text
bbox = draw.textbbox((30, 30), text, font=font)

# You can now use the bbox (bounding box) to determine where to draw the text
draw.text((500, 500), text, font=font, fill="black")

# Optionally, draw the bounding box to visualize it
draw.rectangle(bbox, outline="red", width=2)

# Save the image
image.save("text_on_image.png")

# Display the image
image.show()

