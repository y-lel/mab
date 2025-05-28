# utils/pdf_fingerprint.py

import os
# from utils.stego.encode_lsb import encode_lsb
from utils.stego.insert_into_pdf import insert_stego_image_into_pdf

from utils.stego.encode_lsb import encode_lsb, make_transparent

def fingerprint_pdf(template_path, user_id):
    base_image = "images/base_image.png"
    stego_image = "images/stego_image.png"
    output_pdf = f"tmp/output_with_stego_{user_id}.pdf"

    fingerprint = f"user_{user_id}_fp"
    encode_lsb(base_image, stego_image, fingerprint)
    make_transparent(stego_image, stego_image, opacity=0.3)

    insert_stego_image_into_pdf(template_path, stego_image, output_pdf)
    print(f"[DEBUG] Embedded fingerprint: {fingerprint}")

    return output_pdf