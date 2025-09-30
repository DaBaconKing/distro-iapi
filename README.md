# 🖼️ Image API

This Flask API generates a 700×500 image with:
- Left: uploaded image or image URL
- Right: white rectangle with Montserrat text

## 🔧 Usage

POST `/generate` with:
- `text`: your string
- `image`: file upload (optional)
- `image_url`: URL to image (optional)

Returns: PNG image

## 🛠️ Deploy

Use [Render](https://render.com) with:
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`

Keep it awake with [UptimeRobot](https://uptimerobot.com)
