from flask import Flask, render_template, request
import resume_parser
import skill_matcher

app = Flask(__name__)
result_data = None

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["resume"]
        text = resume_parser.extract_text(file)

        skills = skill_matcher.extract_skills(text)
        score, missing = skill_matcher.calculate_score(skills)

        result = {
            "skills": skills,
            "score": score,
            "missing": missing
        }
    

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)