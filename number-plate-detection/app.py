
from flask import Flask, request, render_template, jsonify
from src.detector import detect_plate
from src.ocr import extract_text_from_image

app = Flask(__name__)

@app.route('/')
def home():
    return "Number Plate Detection API"

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['file']
    file.save("uploaded.jpg")
    image, plate = detect_plate("uploaded.jpg")
    
    if plate is not None:
        plate_text = extract_text_from_image(plate)
        return jsonify({"plate_text": plate_text})
    return jsonify({"error": "No plate detected"})

if __name__ == "__main__":
    app.run(debug=True)
