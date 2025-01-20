from flask import Flask, request, send_file
from PIL import Image
import io
app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Image Colorization App!"

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the request contains a file part
    if 'file' not in request.files:
        return "No file part in the request", 400

    file = request.files['file']

    # Check if a file is actually uploaded
    if file.filename == '':
        return "No file selected", 400

    try:
        # Open the uploaded image
        img = Image.open(file)

        # Process the image (example: resize it to 256x256)
        img = img.resize((256, 256))

        # Save the processed image to a BytesIO object
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        # Send the image back as a response
        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        return f"Error processing image: {str(e)}", 500


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000, debug=True)
