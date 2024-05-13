# Neolocus_Backend_Assignment

Image Processing API written in Python, using the Pillow library for increasing the brightness of an image and exposing the functions with the Flask framework. The API is tested with png and jpg format.

## Getting started

There are three Python files:

- `app.py` - includes the basic calls of the API. Run the file and use the `GET` and `POST` requests on `localhost:5000`.
- `image_processing.py` - includes the function that takes of care of brightening the image.
- `client.py` - a client script to send an image to test the `POST` requests and obtain a response, decode and save the image locally. `app.py` needs to be running.

Other files included are `input_image.png` is the image sent by the client script for testing and `modified_image.jpg` is the resultant image after brightening.

## Dependencies

Python installation requires the `PIL` (Pillow) library for image processing, `flask` and `requests` library. It is recommended to use the `requirements.txt` file
```
pip install -r requirements.txt
```

## Documentation

### Configuration

No additional configuration is needed to run the API in its basic form. However, you can configure the Flask application settings by modifying the `app.run(debug=True)` line in the app.py file.

### Running the API

Start the Flask application by running:

```
python app.py
```
This will start the server on `http://127.0.0.1:5000/` with the `GET` request as default with 'Image Processing API' being displayed on the server. Below is the screenshot of the same:

<img src="https://github.com/AbhishekKolari/Neolocus_Backend_Assignment/assets/72036135/0d74ba0c-affd-4c6d-b374-aa0d74d8db5a" width="800" height="500">

### Using the API

#### Endpoint /modify_image

- **Method** - POST
- **Content-type** - application-type

#### Client Script

With `app.py` still running, run the command:
```
python client.py
```

This will send the `input_image` as request to the API and provide the `modified_image` saved locally on your machine.
To change the input image, replace `input_image.png` in the function call `process_image('input_image.png')` and to save in your own location replace `modified_image.jpg` in the line `with open('modified_image.jpg', 'wb') as f` in the file `client.py`.

## Error Handling

The API provides basic error handling, returning a 400 status code if the image data is not found in the request and a 500 status code for any other errors that occur during processing.

## Image Comparison

The increase in brightness was adjusted by a factor of 30%. The images are shown below for comparison:

<img src="https://github.com/AbhishekKolari/Neolocus_Backend_Assignment/assets/72036135/e51b3a9c-15a6-4b28-85ca-7b0350960b3b" width="400" height="400"> <img src="https://github.com/AbhishekKolari/Neolocus_Backend_Assignment/assets/72036135/2c040382-414f-4382-b222-dd4ea999d2ed" width="400" height="400">

On the left is the input image and the right is the modified image. It is observed that there is a slight increase in brightness, since the brightness factor is not much the increase seems minimal. When increasing the brightness factor in the file `image_processing.py`, the modification produces a brighter image.


 


