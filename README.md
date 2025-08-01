# 🧠 Structura-AI – AI-Powered UML Diagram Generator

Turn your thoughts into software design instantly.  
Structura-AI is a full-stack web application that **automatically generates UML diagrams** (Class, Sequence, Use Case) from **natural language prompts** using GPT-based AI and renders them using Graphviz.

![Structura-AI Demo](https://structura-ai.onrender.com/) <!-- optional: demo gif -->

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
  <img width="1898" height="840" alt="Screenshot 2025-08-02 020119" src="https://github.com/user-attachments/assets/6860d417-0b0d-4160-8986-03082d7f100d" />

- **Generated UML Diagram Preview**
  <img width="1888" height="798" alt="Screenshot 2025-08-02 020319" src="https://github.com/user-attachments/assets/523d76aa-7c1a-4225-a3bc-ecd8592da3b9" />


---

## 🧪 How It Works

1. **User** enters a natural language description (e.g., "A customer places an order that contains items")
2. **Flask Backend** sends prompt to `g4f API` → GPT model parses relationships/entities
3. **Structured UML Syntax** is generated
4. **Graphviz** renders the diagram and sends it back to frontend
5. **React.js UI** displays the live diagram

---

