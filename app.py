import os
import re
import json
import base64
import requests
import logging
import plantuml
import g4f
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'static/diagrams'
USERS_FILE = 'users.json'

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# PlantUML instance
plantuml_instance = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/img/')

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ----------------- Helpers -----------------

def load_users():
    """Load users from users.json"""
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    """Save users to users.json"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def login_required(f):
    """Decorator to protect routes that require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def get_plantuml_themes():
    """List of PlantUML themes"""
    return [
        "amiga", "aws-orange", "black-knight", "bluegray", "blueprint", "carbon-gray",
        "cerulean-outline", "cerulean", "cloudscape-design", "crt-amber", "crt-green",
        "cyborg-outline", "cyborg", "hacker", "lightgray", "mars", "materia-outline",
        "materia", "metal", "mimeograph", "minty", "mono", "none", "plain", "reddress-darkblue",
        "reddress-darkgreen", "reddress-darkorange", "reddress-darkred", "reddress-lightblue",
        "reddress-lightgreen", "reddress-lightorange", "reddress-lightred", "sandstone", "silver",
        "sketchy-outline", "sketchy", "spacelab-white", "spacelab", "sunlust", "superhero-outline",
        "superhero", "toy", "united", "vibrant"
    ]

def generate_ai_prompt(project_name, diagram_type, theme=None):
    theme_directive = f"!theme {theme}\n" if theme else ""
    return f"""Create a PlantUML syntax for a {diagram_type} diagram for a project named {project_name}. 
    The diagram should be detailed and follow UML standards. 
    Provide only the PlantUML syntax without any additional text or explanations.
    Start with @startuml
    {theme_directive}"""

def extract_plantuml_syntax(text):
    """Extract only syntax between @startuml and @enduml"""
    pattern = r'@startuml\s*(.*?)\s*@enduml'
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        raise Exception("No valid PlantUML syntax found in AI response.")
    content = match.group(1).strip()
    return content

def get_ai_response(prompt):
    """Ask AI to generate PlantUML code"""
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return extract_plantuml_syntax(response)
    except Exception as e:
        logger.error(f"AI API Error: {str(e)}")
        raise Exception("Failed to generate diagram syntax from AI.")

def generate_diagram(plantuml_syntax):
    """Generate PNG diagram from PlantUML syntax"""
    try:
        png_data = plantuml_instance.processes(plantuml_syntax)
        return base64.b64encode(png_data).decode()
    except Exception as e:
        logger.error(f"PlantUML Processing Error: {str(e)}")
        raise

# ----------------- Routes -----------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/try')
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            error = 'Username already exists.'
        else:
            users[username] = password
            save_users(users)
            session['username'] = username
            return redirect('/try')
    return render_template('signup.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/try')
@login_required
def try_app():
    diagram_types = [
        "Sequence Diagram", "Use Case Diagram", "Class Diagram", "Object Diagram",
        "Activity Diagram", "Component Diagram", "Deployment Diagram", "State Diagram", "Timing Diagram"
    ]
    themes = get_plantuml_themes()
    return render_template('generate.html', diagram_types=diagram_types, themes=themes)

@app.route('/generate', methods=['POST'])
@login_required
def generate():
    project_name = request.form.get('project_name')
    diagram_type = request.form.get('diagram_type')
    theme = request.form.get('theme')

    if not project_name or not diagram_type:
        return jsonify({'error': 'Missing required fields'}), 400

    prompt = generate_ai_prompt(project_name, diagram_type, theme)
    plantuml_syntax = get_ai_response(prompt)
    
    if theme:
        plantuml_syntax = f"!theme {theme}\n{plantuml_syntax}"

    diagram_base64 = generate_diagram(plantuml_syntax)

    return jsonify({
        'diagram': diagram_base64,
        'syntax': plantuml_syntax
    })

# ----------------- Main -----------------

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

