from flask import Flask, render_template, request
import os
from resume_logic import analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files.get("resume")

        if not file:
            return "No file uploaded"

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        result = analyze_resume(filepath)
        print(result)


        return render_template("result.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
