from PIL import Image

def decode_lsb(image_path):
    img = Image.open(image_path)
    width, height = img.size

    bits = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            bits.append(str(r & 1))
            bits.append(str(g & 1))
            bits.append(str(b & 1))

    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            continue
        char = chr(int(''.join(byte), 2))
        if char == chr(0):  # null terminator means end of message
            break
        chars.append(char)

    message = ''.join(chars)
    return message
