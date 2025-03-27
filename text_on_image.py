import PIL.ImageDraw
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract/tesseract'  # Update with the correct path

from PIL import Image, ImageFont

img = Image.open("images/landscape.jpg")
text_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

draw = PIL.ImageDraw.Draw(img)

PIL.ImageDraw.Draw(img)

font = ImageFont.load_default()

#font = ImageFont.truetype("/path/to/arial.ttf", 40)
#font = ImageFont.truetype("arial.ttf", 40)

text = "Hello World"

image_width, image_height = img.size

if text_data["text"]:
    for i, text in enumerate(text_data["text"]):
        if text.strip():  # Ensure the text isn't empty
            bbox = (text_data["left"][i], text_data["top"][i],
                    text_data["left"][i] + text_data["width"][i],
                    text_data["top"][i] + text_data["height"][i])

            # Calculate width of the bounding box
            text_width = bbox[2] - bbox[0]
            print(f"Text: {text}, Bounding box: {bbox}, Width: {text_width}")
else:
    print("No text detected.")

bbox = draw.textbox((0,0),text,font=font)

text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x= (image_width - text_width) / 2
y= (image_height - text_height) / 2

#text_width, text_height = font(text,font=font)

draw.text((image_width/2, image_height/2), text, font=font, fill="white")

img.show()
img.save("output.png")








