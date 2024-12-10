
import pytesseract
from PIL import Image
import cv2

def extract_text_from_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    cv2.imwrite("temp_plate.png", binary)
    text = pytesseract.image_to_string("temp_plate.png", lang='eng')
    return text.strip()
