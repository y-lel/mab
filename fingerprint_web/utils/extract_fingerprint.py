import fitz  # PyMuPDF
from utils.stego.decode_lsb import decode_lsb
from utils.docx_fingerprint import extract_fingerprint_from_docx

def extract_fingerprint_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    for page in doc:
        images = page.get_images(full=True)
        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            with open(f"tmp/temp_img.{ext}", "wb") as f:
                f.write(image_bytes)
            fingerprint = decode_lsb(f"tmp/temp_img.{ext}")
            if fingerprint:
                return fingerprint
    return None

def extract_fingerprint(file_path, file_type):
    if file_type == 'pdf':
        return extract_fingerprint_from_pdf(file_path)
    elif file_type == 'docx':
        from utils.stego.decode_lsb import decode_lsb
        return extract_fingerprint_from_docx(file_path, decode_lsb)
    else:
        return None
