from PIL import Image, ImageEnhance
import io

def adjust_brightness(image_bytes, brightness_factor=1.3):  #default brightness factor is 1.3 which is an increase by 30%
    image = Image.open(io.BytesIO(image_bytes))
    # Adjust brightness
    # image = image.point(lambda p: p * brightness_factor)  # pixel-wise multiplication
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)
    output_buffer = io.BytesIO()
    image.save(output_buffer, format="JPEG")
    return output_buffer.getvalue()