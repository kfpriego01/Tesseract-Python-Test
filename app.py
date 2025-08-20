from PIL import Image
import pytesseract

# Tell pytesseract where tesseract.exe is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load an image
image = Image.open("IvV2y.png")

# Extract text
text = pytesseract.image_to_string(image)

print("Extracted Text:")
print(text
