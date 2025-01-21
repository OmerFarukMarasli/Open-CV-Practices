from PIL import Image
import pytesseract as pt

img = Image.open("contour (1).png")
text = pt.image_to_string(img,lang="tr")
print(text)