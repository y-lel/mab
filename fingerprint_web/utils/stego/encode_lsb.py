# utils/stego/encode_lsb.py
from PIL import Image, ImageEnhance

def encode_lsb(image_path, output_path, message):
    img = Image.open(image_path).convert('RGB')
    encoded = img.copy()
    width, height = img.size

    message += chr(0)  # null terminator
    bits = ''.join([format(ord(c), '08b') for c in message])
    bit_idx = 0

    for y in range(height):
        for x in range(width):
            if bit_idx >= len(bits):
                encoded.save(output_path)
                return

            r, g, b = encoded.getpixel((x, y))

            if bit_idx < len(bits):
                r = (r & ~1) | int(bits[bit_idx])
                bit_idx += 1
            if bit_idx < len(bits):
                g = (g & ~1) | int(bits[bit_idx])
                bit_idx += 1
            if bit_idx < len(bits):
                b = (b & ~1) | int(bits[bit_idx])
                bit_idx += 1

            encoded.putpixel((x, y), (r, g, b))

    encoded.save(output_path)

def make_transparent(image_path, output_path, opacity=0.3):
    img = Image.open(image_path).convert("RGBA")
    alpha = img.split()[3]
    alpha = alpha.point(lambda p: int(p * opacity))
    img.putalpha(alpha)
    img.save(output_path)
