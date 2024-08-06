from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Debug logging
        print(f"Received file: {file.filename}, Type: {file.mimetype}, Size: {len(file.read())} bytes")
        file.seek(0)  # Reset file pointer after reading size

        image = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(image)
        return jsonify({'text': text})
    except Exception as e:
        # Debug logging
        print(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
