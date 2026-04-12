import os
import sys
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

# Fix import path (important for Render)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import extract_text_from_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return "Resume Parser is running 🚀"


@app.route("/upload", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Extract text using models.py
        extracted_text = extract_text_from_resume(filepath)

        return jsonify({
            "message": "File processed successfully",
            "extracted_text": extracted_text[:1000]  # limit output
        })

    return jsonify({"error": "Invalid file type"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
