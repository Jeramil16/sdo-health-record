
import qrcode
import os

def generate_qr_code(token: str):
    url = f"http://example.com/view/{token}"
    img = qrcode.make(url)
    path = f"app/static/qr/{token}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    return f"/static/qr/{token}.png"
