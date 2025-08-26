import os
from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv

# Load .env file in local dev (Render will already provide env vars)
load_dotenv()

app = Flask(__name__)

# Set API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    return render_template("generate.html", uml_code=None)

@app.route("/generate_from_text", methods=["POST"])
def generate_from_text():
    description = request.form.get("uml_desc", "")

    if not description.strip():
        return render_template(
            "generate.html",
            uml_code="⚠️ Please enter a valid description."
        )

    prompt = f"""
    Convert the following description into PlantUML code for a UML diagram.
    Only return valid PlantUML code wrapped between @startuml and @enduml.
    Description: {description}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # you can switch to gpt-4o or gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        plantuml_code = response.choices[0].message["content"].strip()

        return render_template("generate.html", uml_code=plantuml_code)

    except Exception as e:
        return render_template(
            "generate.html",
            uml_code=f"⚠️ Error occurred: {str(e)}"
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
