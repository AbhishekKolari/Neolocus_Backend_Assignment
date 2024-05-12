import requests
import base64
# from PIL import Image
# import io

def process_image(image_path):
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
        image_b64 = base64.b64encode(image_bytes).decode('utf-8')


    data = {'image': image_b64}
    response = requests.post('http://localhost:5000/modify_image', json=data)

    if response.status_code == 200:
        modified_image_b64 = response.json()['modified_image']
        modified_image_bytes = base64.b64decode(modified_image_b64)
        with open('modified_image.jpg', 'wb') as f:
            f.write(modified_image_bytes)
        print("Modified image saved as modified_image.jpg")
    else:
        print("Error:", response.json()['error'])

process_image('input_image.png')