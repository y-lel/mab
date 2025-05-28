from flask import Flask, render_template, send_file, request
import os
from utils.pdf_fingerprint import fingerprint_pdf
from utils.epub_fingerprint import fingerprint_epub
# from utils.docx_fingerprint import fingerprint_docx
# from utils.extract_fingerprint import extract_fingerprint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download/pdf")
def download_pdf():
    user_id = request.args.get("user_id", "guest")
    output_path = fingerprint_pdf("templates_files/template.pdf", user_id)
    return send_file(output_path, as_attachment=True)

@app.route("/download/epub")
def download_epub():
    user_id = request.args.get("user_id", "guest")
    output_path = fingerprint_epub("templates_files/template.epub", user_id)
    return send_file(output_path, as_attachment=True)

@app.route("/download/docx")
# def download_docx():
#     user_id = request.args.get("user_id", "guest")
#     output_path = fingerprint_docx("templates_files/template.docx", user_id)
#     return send_file(output_path, as_attachment=True)

@app.route("/extract_fingerprint", methods=["POST"])
def extract_fp():
    # Upload a suspicious file (PDF or DOCX)
    uploaded_file = request.files.get("file")
    if not uploaded_file:
        return {"error": "No file uploaded"}, 400

    file_type = None
    filename = uploaded_file.filename.lower()
    if filename.endswith(".pdf"):
        file_type = "pdf"
    elif filename.endswith(".docx"):
        file_type = "docx"
    else:
        return {"error": "Unsupported file type"}, 400

    temp_path = f"tmp/{uploaded_file.filename}"
    uploaded_file.save(temp_path)

    # fingerprint = extract_fingerprint(temp_path, file_type)
    # os.remove(temp_path)

    # if fingerprint:
    #     return {"fingerprint": fingerprint}
    # else:
    #     return {"error": "Fingerprint not found"}

if __name__ == "__main__":
    app.run(debug=True)
