from utils.stego.decode_lsb import decode_lsb
from utils.extract_fingerprint import extract_fingerprint  # your function that extracts image & decodes it

output_file = "tmp/output_with_stego_8956.pdf"  # or docx
decoded_fp = extract_fingerprint(output_file, "pdf")  # or "docx"
print(f"[DEBUG] Decoded fingerprint immediately after embedding: {decoded_fp}")
