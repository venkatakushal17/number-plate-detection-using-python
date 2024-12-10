
import cv2

CASCADE_PATH = "models/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def detect_plate(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    plates = plate_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cropped_plate = img[y:y+h, x:x+w]
        return img, cropped_plate

    return img, None
