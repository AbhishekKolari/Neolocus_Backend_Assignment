from flask import Flask, request, jsonify
import base64
from image_processing import adjust_brightness

app = Flask(__name__)

@app.route('/')   # default route
def index():
    return 'Image Processing API'


@app.route('/modify_image', methods=['POST'])
def modify_image():
    try:
        data = request.json
        if 'image' not in data:
            return jsonify({'error': 'Image data not found'}), 400

        image_bytes = base64.b64decode(data['image']) #decode from base64 to image bytes
        modified_image_bytes = adjust_brightness(image_bytes)
        modified_image_b64 = base64.b64encode(modified_image_bytes).decode('utf-8') #encode into base64 and convert into UTF-8 string
        return jsonify({'modified_image': modified_image_b64}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)