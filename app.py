from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io, requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Image API is running!'

@app.route('/generate', methods=['POST'])
def generate_image():
    text = request.form.get('text', 'Hello')
    image_file = request.files.get('image')
    image_url = request.form.get('image_url')

    # Load image
    if image_file:
        img = Image.open(image_file)
    elif image_url:
        img = Image.open(io.BytesIO(requests.get(image_url).content))
    else:
        return "No image provided", 400

    # Resize/crop image to 350x500
    img = img.convert("RGB").resize((350, 500))

    # Create canvas
    canvas = Image.new("RGB", (700, 500), "black")
    canvas.paste(img, (0, 0))

    # Draw white rectangle
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([350, 0, 700, 500], fill="white")

    # Load Montserrat font
    try:
        font = ImageFont.truetype("Montserrat-Regular.ttf", 40)
    except:
        font = ImageFont.load_default()

    # Draw text
    draw.text((370, 200), text, font=font, fill="black")

    # Return image
    buf = io.BytesIO()
    canvas.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
