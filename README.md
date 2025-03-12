OCR based Answer Extraction and Grading System.

Welcome to the Answer Extraction and Grading System! This Python-based project uses Optical Character Recognition (OCR) to read multiple-choice answer sheets and evaluate them. It compares extracted answers with the predefined correct answers, calculates a score, and provides feedback with a grade.

Features:
Text Extraction with OCR: The project uses Tesseract OCR to extract text from images of answer sheets.
Answer Parsing: It identifies and pulls out multiple-choice answers (like A, B, C, D) from the OCR output.
Score Calculation: The system compares extracted answers with predefined correct answers and calculates a score.
Grading System: Based on the score, the program assigns a grade (A, B, or C) and provides feedback.
Tech Stack 💻
This project is built with the following Python libraries:

OpenCV: For image processing (e.g., converting images to grayscale, thresholding).
pytesseract: The magic behind extracting text from images using OCR.
NumPy: For handling arrays and performing mathematical operations (useful for image processing).
Matplotlib: For visualizing or debugging images and text extraction (optional, can be expanded in future).
Regular Expressions (re): For parsing answers from the extracted text.

Installation :
Clone the repository:
git clone https://github.com/yourusername/project-name.git
cd project-name
Install the required dependencies:

Create a requirements.txt file with the following content (if you don’t have one yet):
opencv-python
pytesseract
numpy
matplotlib

Then install them using:
pip install -r requirements.txt
Install Tesseract:

You’ll need Tesseract installed on your system for OCR functionality. Follow the instructions for your platform:

Windows: Download the installer from Tesseract GitHub.
Mac: Use Homebrew: brew install tesseract.
Linux: Install via package manager: sudo apt install tesseract-ocr.
After installation, make sure to set the Tesseract executable path in your script (if required).

Usage
Prepare the image: Place the image containing the answer sheet in the images/ folder. The image should have clear, typed answers (works best with typed text for now).

Update the image path: Modify the image_path variable in the script to point to your image file.

Run the script:
python main.py

The program will extract the answers from the image, compare them with the predefined answers, calculate a score, and assign a grade. The feedback and grade will be displayed in the console.

Example Output:
https://github.com/tanishka-kaur09/OCR-Model-project/blob/main/Screenshot%202025-03-12%20223430.png

Limitations: Currently, only answers in the form of A, B, C, or D are supported. Future updates will enhance the functionality to handle more complex answer sheets and handwritten text

Future Scope 
Right now, the system works with typed text only, meaning it is optimized for machine-printed answer sheets. However, in the future, we aim to extend the project to work with handwritten text as well! We plan to:

Implement advanced OCR techniques for better recognition of handwritten answers.
Train custom machine learning models for handwritten text recognition to improve accuracy and support a wider range of answer sheets.
