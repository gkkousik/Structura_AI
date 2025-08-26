from flask import Flask, render_template, request, redirect, url_for, session
from openai import OpenAI
import os
import json

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_secret")  # load from env in production

# Load users
if os.path.exists("users.json"):
    with open("users.json", "r") as f:
        users = json.load(f)
else:
    users = {}

# Configure OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("generate"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users:
            return render_template("signup.html", error="User already exists")
        else:
            users[username] = password
            with open("users.json", "w") as f:
                json.dump(users, f)
            return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/generate")
def generate():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("generate.html")

@app.route("/generate_from_text", methods=["POST"])
def generate_from_text():
    if "user" not in session:
        return redirect(url_for("login"))

    description = request.form.get("uml_desc")

    prompt = f"""
    Convert the following description into PlantUML code for a UML diagram:
    Description: {description}
    Only return valid PlantUML code between @startuml and @enduml.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # change to gpt-4o / gpt-5 if enabled
            messages=[{"role": "user", "content": prompt}]
        )
        plantuml_code = response.choices[0].message.content.strip()

        return render_template("generate.html", uml_code=plantuml_code)

    except Exception as e:
        print("Error:", e)  # log for debugging
        return render_template("generate.html", uml_code=f"Error generating diagram: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
