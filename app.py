from services.static_analysis import estimate_complexity
from flask import Flask, render_template, request, jsonify
from services.ai_service import analyze_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.json["code"]
    static_result = estimate_complexity(code)
    ai_result = analyze_code(code)

    combined = f"""
Static Complexity Estimate: {static_result}

-----------------------------------

AI Analysis:
{ai_result}
"""

    return jsonify({"result": combined})


if __name__ == "__main__":
    app.run(debug=True)
