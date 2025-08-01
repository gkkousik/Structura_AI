# 🧠 Structura-AI – AI-Powered UML Diagram Generator

Turn your thoughts into software design instantly.  
Structura-AI is a full-stack web application that **automatically generates UML diagrams** (Class, Sequence, Use Case) from **natural language prompts** using GPT-based AI and renders them using Graphviz.

![Structura-AI Demo](https://your-demo-link.com/preview.gif) <!-- optional: demo gif -->

---

## 🚀 Why Structura-AI?

Tired of dragging boxes and arrows manually?

Structura-AI is built for:
- 🧑‍💻 Developers who want faster design iterations
- 🎓 Students learning object-oriented modeling
- 📊 Analysts and PMs needing visual architecture from requirements
- 💡 Startups & teams building rapid prototypes

---

## ⚙️ Tech Stack

| Layer          | Technologies                           |
|----------------|----------------------------------------|
| Frontend       | React.js, Tailwind CSS                 |
| Backend        | Python, Flask, RESTful APIs            |
| AI Integration | GPT-based NLP via g4f API              |
| Rendering      | Graphviz for UML diagram generation    |
| Auth & Deploy  | Firebase Authentication, Render, GitHub Actions |

---

## 🧩 Features

✅ Generate Class, Sequence, and Use Case diagrams from plain English  
✅ Real-time diagram rendering using Graphviz  
✅ Download diagrams as PNG  
✅ Secure login via Firebase  
✅ CI/CD with GitHub Actions  
✅ Deployed & accessible on all browsers

---

## 📸 Screenshots

> Replace with real images or links to hosted screenshots

- **Prompt Input Interface**  
- **Generated UML Diagram Preview**  
- **Responsive Design on Desktop & Mobile**

---

## 🧪 How It Works

1. **User** enters a natural language description (e.g., "A customer places an order that contains items")
2. **Flask Backend** sends prompt to `g4f API` → GPT model parses relationships/entities
3. **Structured UML Syntax** is generated
4. **Graphviz** renders the diagram and sends it back to frontend
5. **React.js UI** displays the live diagram

---

## 🔧 Local Setup

```bash
# Clone repo
git clone https://github.com/your-username/structura-ai.git
cd structura-ai

# Setup backend
cd backend
pip install -r requirements.txt
python app.py

# Setup frontend (in another terminal)
cd frontend
npm install
npm start
