from utils.stego.encode_lsb import encode_lsb, make_transparent
from utils.stego.decode_lsb import decode_lsb

input_img = "images/base_image.png"
output_img = "images/stego_image.png"
fingerprint = "user123_fp"

# Encode
encode_lsb(input_img, output_img, fingerprint)
make_transparent(output_img, output_img, opacity=0.3)
print("✅ Fingerprint embedded.")

# Decode
extracted = decode_lsb(output_img)
if extracted:
    print(f"✅ Fingerprint extracted: {extracted}")
else:
    print("❌ No fingerprint found.")
