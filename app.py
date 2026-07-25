import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from analyzer.parser import parse_resume
from analyzer.ats_scorer import calculate_ats_score
from analyzer.ai_feedback import generate_ai_feedback

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5MB limit
ALLOWED_EXTENSIONS = {"pdf", "docx"}

os.makedirs("uploads", exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    # --- Validate inputs ---
    if "resume" not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    file = request.files["resume"]
    jd_text = request.form.get("job_description", "").strip()

    if not jd_text:
        return jsonify({"error": "Job description is required"}), 400
    if file.filename == "" or not allowed_file(file.filename):
        return jsonify({"error": "Only PDF or DOCX files are allowed"}), 400

    # --- Save & Parse ---
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    resume_text = parse_resume(filepath)
    os.remove(filepath)  # Clean up after parsing

    if not resume_text:
        return jsonify({"error": "Could not extract text from resume"}), 422

    # --- Score & Feedback ---
    ats_data = calculate_ats_score(resume_text, jd_text)
    ai_feedback = generate_ai_feedback(resume_text, jd_text, ats_data)

    return render_template("result.html", ats=ats_data, feedback=ai_feedback)


if __name__ == "__main__":
    app.run(debug=True)
