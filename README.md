---

# Number Plate Detection Using Python

This project implements a Number Plate Detection system using Python, OpenCV, and OCR (Optical Character Recognition). The system detects vehicle number plates from images or live video feeds and extracts the text from them.

---

## **Features**
- Detects number plates from images or videos using Haar Cascades.
- Extracts text from number plates using Tesseract OCR.
- Easy-to-use interface built with Flask (optional).

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - OpenCV (for image processing and plate detection)
  - pytesseract (for OCR)
  - Flask (for building a web interface)
- **Model**: Haar Cascade for Russian plate detection (can be customized for other regions).

---

## **Installation**

### Prerequisites
Ensure you have the following installed:
- Python 3.8+  
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/number-plate-detection.git
cd number-plate-detection
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install Tesseract OCR
- Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
- Note the installation path. Update it in the code if needed.

---

## **Usage**

### Running the Application
1. **Run the script**:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

### Detecting Number Plates
- **For Images**:
  - Place your test images in the `datasets` folder.
  - Update the `app.py` or `src/detector.py` with the image path.
- **For Video**:
  - Use a webcam or provide a video file as input.

---

## **Project Structure**
```
number-plate-detection/
├── app.py                   # Flask application file
├── datasets/                # Sample dataset (e.g., car images)
│   └── car.jpg
├── models/
│   └── haarcascade_russian_plate_number.xml # Haar Cascade Model
├── requirements.txt         # Dependencies list
├── src/                     # Source code folder
│   ├── detector.py          # Detection logic
│   └── ocr.py               # OCR extraction logic
├── README.md                # Project documentation
```

---

## **Future Enhancements**
- Add support for live video streams from IP cameras.
- Enhance detection for multi-language plates.
- Integrate deep learning-based detection models for higher accuracy.

---

## **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## **License**
This project is open-source and licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgements**
- OpenCV for image processing.
- Tesseract OCR for text recognition.
- Haar Cascades for object detection.

---
