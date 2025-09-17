# 🧠 Structura-AI – AI-Powered UML Diagram Generator

Turn your thoughts into clean software design, instantly.  
Structura-AI is a full-stack web application that **automatically generates UML diagrams** (Class, Use Case, Sequence) from **natural language prompts** using GPT-based AI and Graphviz rendering.

<img src="https://github.com/user-attachments/assets/54a0ad77-f32a-4273-8847-2a87d9314807" alt="UML Banner" width="800" height="700"/>




---

## 🌐 Live Demo

🚀 Access the application here → **[https://structura-ai.onrender.com/](https://structura-ai.onrender.com/)**  
🟢 Try generating your first diagram now!

---

## 📌 Why Structura-AI?

Designing UML diagrams shouldn't be a bottleneck. Structura-AI empowers you to:
- ✍️ **Describe in plain English**, and get fully-structured UML diagrams instantly.
- 🛠️ **Reduce manual effort by ~90%** in the software design phase.
- 🌍 Enable **non-technical stakeholders** to visualize system architecture.
- ⚙️ Enhance **software modeling in education, startups, and agile teams**.

---

## ⚙️ Tech Stack

| Layer             | Technologies                            |
|-------------------|------------------------------------------|
| **Frontend**       | React.js, Tailwind CSS                   |
| **Backend**        | Python (Flask), RESTful APIs             |
| **AI Engine**      | GPT-based NLP via g4f API                |
| **Rendering**      | Graphviz for UML diagram generation      |
| **Auth & DevOps**  | Firebase Auth, Render.com, GitHub Actions |

---

## 🧩 Features

- 🧠 **AI-Powered UML Generation** (Class, Use Case, Sequence)
- ⏱️ **Real-Time Rendering** via Graphviz in < 20 seconds
- 📥 **Download Diagrams** in PNG format
- 🔐 **User Authentication** with Firebase
- 🌍 **Responsive UI** – Works on desktops, tablets, and phones
- 🚀 **CI/CD Integrated** – Auto-deploy with GitHub Actions
- 📊 **Google Analytics** for tracking user engagement

---

## 🖼️ Screenshots

| Prompt Input Panel                                                                                   | UML Diagram Output                                                                                   | Mobile View                                                                                             |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| (<img width="649" height="552" alt="image" src="https://github.com/user-attachments/assets/61676248-51c1-4d4f-b700-24502aba46b2" />    | (<img width="934" height="721" alt="image" src="https://github.com/user-attachments/assets/32acbc03-7ad3-4c67-8944-170dfaa67f90" />    | (![WhatsApp Image 2025-09-17 at 19 17 14_274a80e5](https://github.com/user-attachments/assets/cdf00602-2ef2-4446-aa30-1f999329f612)
)          |

---

## 🔄 How It Works

flowchart TD
    A[User Prompt in Natural Language] --> B[Frontend (React.js)]
    B --> C[Flask Backend API]
    C --> D[g4f API (GPT-based NLP)]
    D --> E[Structured UML Syntax]
    E --> F[Graphviz Renderer]
    F --> G[UML Diagram Output]
    G --> B

