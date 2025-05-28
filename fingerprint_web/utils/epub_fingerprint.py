import zipfile
import os
import shutil
import tempfile
from datetime import datetime
import hashlib

TMP_DIR = "tmp"

def fingerprint_epub(input_epub_path, user_id):
    timestamp = datetime.utcnow().isoformat()
    raw_fp = f"{user_id}_{timestamp}"
    fingerprint = hashlib.sha256(raw_fp.encode()).hexdigest()[:12]

    # Unpack EPUB
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(input_epub_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # Inject fingerprint in metadata (content.opf)
    content_file = None
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file.endswith(".opf"):
                content_file = os.path.join(root, file)
                break

    if content_file:
        with open(content_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "<metadata>" in content:
            content = content.replace(
                "<metadata>",
                f"<metadata><meta name=\"fingerprint\" content=\"{fingerprint}\"/>",
                1
            )
        with open(content_file, "w", encoding="utf-8") as f:
            f.write(content)

    # Repack into new EPUB
    output_path = os.path.join(TMP_DIR, f"{fingerprint}.epub")
    with zipfile.ZipFile(output_path, 'w') as new_zip:
        for foldername, subfolders, filenames in os.walk(temp_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, temp_dir)
                new_zip.write(file_path, arcname)

    shutil.rmtree(temp_dir)
    return output_path
