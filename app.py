from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'K89147936588957'

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(image)
        
        # Use OpenAI to process the OCR text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another model you have access to
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ]
        )
        chat_response = response.choices[0].message['content']
        
        return jsonify({'text': text, 'openai_response': chat_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
