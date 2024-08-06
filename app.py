from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io
import openai

app = Flask(__name__)

# Configure OpenAI API Key
openai.api_key = 'K89147936588957'

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Process the image
        image = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(image)
        
        # Ask OpenAI about the extracted text
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the OpenAI model you want to use
            prompt=f"Here is some text extracted from an image: '{text}'. Can you provide more information or answer questions based on this text?",
            max_tokens=150
        )
        
        # Return the OpenAI response
        openai_text = response.choices[0].text.strip()
        
        return jsonify({
            'text': text,
            'openai_response': openai_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
